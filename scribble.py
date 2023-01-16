# given 5 cards, find the number of combinations giving 15 as sum
# Input example:
# 3 5 7 10 11

cards = [3, 5, 7, 10, 11]
res = 0


def scribble(cards):
    '''build all possible combinations of cards using binary numbers 1-31'''
    res = 0
    for i in range(1, 32):
        s = ('0' * 5 + bin(i)[2:])[-5:]
        if sum([cards[k] for k in range(5) if s[k] == '1']) == 15:
            res += 1
    return res


print(scribble(cards))

import itertools


def scribble2(cards):
    '''build all possible combinations of cards using itertools'''
    res = 0
    for i in range(1, 6):
        for comb in itertools.combinations(cards, i):
            print(i, comb)
            if sum(comb) == 15:
                res += 1
    return res


print(scribble2(cards))


def scribble3(cards):
    '''build all possible combinations of cards using itertools'''
    res = 0
    for i in range(1, 6):
        for comb in itertools.starmap(cards, i):
            if sum(comb) == 15:
                res += 1
    return res
