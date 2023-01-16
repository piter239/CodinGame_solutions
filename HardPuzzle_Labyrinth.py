# https://www.codingame.com/ide/puzzle/the-labyrinth
#
# TODO: study other good solutions
#
# The Labyrinth
# path-finding on 2D map
# the map is a string of length rows * columns
# i, ti, ci, ki are indexes of positions in the map == x_coord * columns + y_coord

import sys
import heapq
from collections import defaultdict

DEBUG = 1


def p(*s):
    """print to stderr for debugging"""
    if DEBUG:
        print(*s, file=sys.stderr, flush=True)


def pm(a_map):
    """ print a map to stderr"""
    # global c
    for i in range(0, len(a_map), columns):
        p(a_map[i: i + columns])


def pdict(d):
    """print a dictionary like a map for debugging"""
    for i in range(rows):
        p(*(d[coord(i, j)] for j in range(columns)))
    p()


# rows: number of rows.
# columns: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
rows, columns, alarm_duration = [int(i) for i in input().split()]
p(rows, columns, alarm_duration)

UP, DOWN, LEFT, RIGHT, HOME = -columns, columns, -1, 1, 0
DIR = {UP: "UP", DOWN: "DOWN", LEFT: "LEFT", RIGHT: "RIGHT", HOME: 'H'}
DIRS = [UP, RIGHT, DOWN, LEFT]


def dijkstra(start_i, get_moves, dist=None, dir=None):
    """calculate the shortest path from start_i to all other reachable nodes
    get moves - a function that returns a list of possible moves from a given node.
    Following arguments can be passed to update the global dist and dir instead of creating new ones:
    dist - a dictionary containing the distances from start_i to a reachable node
    dir - a dictionary containing direction from reachable nodes towards start_i
    """

    p("DIJKSTRA in from", start_i)

    if not dist:
        dist = defaultdict(lambda: rows * columns * 2)
    if not dir:
        dir = defaultdict(lambda: HOME)

    dist[start_i] = 0

    q = [(0, start_i)]
    while q:
        # p(q)
        d, i = heapq.heappop(q)
        if d > dist[i]:
            continue
        for next_i in get_moves(i):
            if dist[next_i] > dist[i] + 1:
                dist[next_i] = dist[i] + 1
                dir[next_i] = i - next_i
                heapq.heappush(q, (dist[next_i], next_i))
    return dist, dir


def neighbors(curr_i, explore=True):
    """return a list of neighbors of curr_i
        if explore == True, '?' is considered a neighbor of any '.CT' but not of another '?'
    """
    can_go_through = '.kCT'
    can_go_through += '?' if explore else ''
    if map[curr_i] in '.kCT':
        return [curr_i + d_i for d_i in DIRS if map[curr_i + d_i] in can_go_through]
    else:
        return []


def speed_moves(x):
    return neighbors(x, explore=False)  # only go through known nodes


def best_way(curr_i, goal_i, get_moves=neighbors, dist=None, dir=None):
    """ return the shortest way as a list containing UP, DOWN, LEFT, RIGHT
        starting from curr_i to reach the goal_i using the currently known map"""
    if '#' in map[curr_i] + map[goal_i]:
        p("cannot go through walls", curr_i, goal_i)
        p(divmod(curr_i, columns), divmod(goal_i, columns))
        pm(map)
        raise Exception

    if not dist:
        dist, dir = dijkstra(curr_i, get_moves)

    path = []
    while goal_i != curr_i:
        path += [-dir[goal_i]]
        goal_i += dir[goal_i]

    return path[::-1]


ti = None  # coordinate of Teleport
ci = None  # coordinate of Command room


def coord(row, column):
    """convert row, column to a single index"""
    return row * columns + column


# map, dist, dir
map = ""

alarm = False  # was the Controlroom reached
g_dist = None  # distance from T to all reachable nodes
g_dir = None  # direction from all reachable nodes to T

run_to_c = False  # is the Controlroom located with path to T <= a
path2c = []

path2explore = []  # is there a goal '?' with path to it?

# game loop
while True:
    # kr: row where Rick is located.
    # kc: column where Rick is located.
    kr, kc = [int(i) for i in input().split()]
    ki = coord(kr, kc)
    if not ti:  # Rick starts at Teleport ))
        ti = ki

    pmap, map = map, ''  # save the previous map and input the new one
    # pmap can be used to check if the map has changed

    for i in range(rows):
        next_row = input()
        if i == kr:
            next_row = next_row[:kc] + 'k' + next_row[kc + 1:]
        map += next_row  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
    pm(map)

    g_dist, g_dir = dijkstra(ti, neighbors)
    for i, cc in enumerate(map):
        if cc == 'C':
            ci = i
            pdict(g_dist)
            if g_dist[i] <= alarm_duration:
                run_to_c = True
            # print(DIR[dd])
            break  # go for it - we know the way!
    p("Currently", ti, ci, ki, alarm_duration, alarm, run_to_c, path2c, path2explore)

    if alarm:  # if the alarm is on, run to the Teleport
        print(DIR[g_dir[ki]])
        continue
    if run_to_c:  # if the Controlroom is found, and we have a path to reach it BEFORE the alarm goes off
        if not path2c:  # if we have not yet calculated the path to the Controlroom
            path2c = best_way(ki, ci, speed_moves)
            p(path2c)
        first, *path2c = path2c
        print(DIR[first])
        if not path2c:  # if we have reached the Controlroom
            run_to_c = False
            alarm = True
        continue

    # If we are here, we have not yet found the Controlroom.
    # We need to explore the nearest '?' nodes.
    # find the nearest '?' node
    if not path2explore:  # if we have not yet calculated the path to the nearest '?'
        dist, dir = dijkstra(ki, neighbors)
        pdict(dist)
        pdict(dir)
        i = min((i for i, c in enumerate(map) if c == '?'), key=dist.get)
        path2explore = best_way(ki, i, neighbors, dist, dir)[:-1]
    first, *path2explore = path2explore
    print(DIR[first])
