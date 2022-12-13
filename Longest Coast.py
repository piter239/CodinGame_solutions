# https://www.codingame.com/training/easy/longest-coast
#  The Longest Coast
#
# Given a n*n grid, output the index of the island with the longest coast, followed by the amount of water it holds.
# (Island indexes are 1-indexed)
#
# An island is made of one or more # characters, we'll call that an island block. While water is represented by ~.
#
# We start from the first row and go through the columns left to right till the last row,
# when encountering a block that you haven't visited yet, that means it is the start of a new island,
# therefore that is now the ith island, it may connect other blocks in four directions:
# up, down, left and right, meaning only horizontal and vertical directions.
# these blocks may also connect other blocks, this goes on until there are no other connected blocks,
# and once there is no connection anymore, we look for a new island using the same process.
#
# If multiple islands have the same amount of water, output the one with a smaller index.
#
# Example:
#
# With n = 5:
#
# ~~~~#
# ~~~##
# ~~~~~
# ~##~~
# ~~~~~
#
# We see that the 2nd island is the one with the longest coast, because the first block is surrounded by 3 water blocks
# and so is the second block. once summed up we get 6, which is greater than the first island having only 4.
# so in this case, we output 2 6 (island 2, 6 water blocks).

import sys


# debugging print to stderr
def print_debug(*args):
    # print(*args, file=sys.stderr, flush=True)
    pass


# Read the standard input according to the problem statement.
def read_input():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    return n, grid


# possible moves as tuple of tuples
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))


# output grid to stdout for debugging
def print_grid(grid):
    for row in grid:
        print_debug(''.join(row))


# calculate the number of water blocks surrounding a single block
# this is a helper function for calculate_island_water
# a set of counted water blocks is returned to avoid double counting
def calculate_water(grid, i, j, counted_water):
    water = 0
    for dx, dy in moves:
        if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid):
            x1, y1 = i + dx, j + dy
            if grid[x1][y1] == '~' and (x1, y1) not in counted_water:
                water += 1
                counted_water.add((x1, y1))
    print_debug("In calculate_water\n")
    print_grid(grid)
    return water, counted_water


# calculate the number of water blocks surrounding an island
# mark the  visited blocks as ' ' to avoid double counting
def calculate_island_water(grid, i, j, counted_water):
    water = 0
    if grid[i][j] == '#':
        plus_water, counted_water = calculate_water(grid, i, j, counted_water)
        water += plus_water
        print_debug("In calculate_island_water\n")
        print_grid(grid)
        grid[i][j] = ' '
        for dx, dy in moves:
            if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid):
                if grid[i + dx][j + dy] == '#':
                    plus_water, counted_water = calculate_island_water(grid, i + dx, j + dy, counted_water)
                    water += plus_water
    return water, counted_water


# find the island with the longest coast
def find_longest_coast(grid):
    max_water = -1
    max_water_index = 0
    found_island_index = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                found_island_index += 1
                water, _ = calculate_island_water(grid, i, j, set())
                if water > max_water:
                    max_water = water
                    max_water_index = found_island_index
    return max_water_index, max_water


n, grid = read_input()
# Write the standard output according to the problem statement.
print(*find_longest_coast(grid))

'''
# Test cases
1.

6
##~~#~
##~~~~
~~~~#~
~~~##~
~####~
~~~~~~

3 12

2.

6
~~~~~~
~~~~#~
~~~##~
~####~
~~~~~~
~~~~~~

1 12

3.

6
~~~~~~
~~~~~~
~~~~#~
~~~##~
~~~~~~
~~~~~~

1 7

4.

5
#~#~#
~#~#~
#~#~#
~#~#~
#~#~#

4 4

5.

5
~~#~~
~#~#~
#~#~#
~#~#~
#~#~#

4 4

'''
