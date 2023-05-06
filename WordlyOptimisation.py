# import WordlyData as wd
# This is an adaptation of an online game Wordle (https://www.nytimes.com/games/wordle/index.html) with slight modifications in the rules.
#
# The goal of the game is to guess the hidden word based on the hints given each turn.
#  	Rules
# At each turn, the player will guess a word.
# After each guess, the player will know the state of each letter.
# Letter at a position can have four states:
# State 1 means the letter at the position is not present in the word.
# State 2 means the letter at the position is present in the word but position is incorrect.
# State 3 means the letter at the position is present in the word and position is correct.
# State 0 means unknown. For the first turn only.
# A letter can appear multiple times in the word.
# Same letter twice or multiple times in the word will work as follows:
# If ORBIT is the word and player guessed ABBEY, B at the 2nd position has state 2 and B at the 3rd position has state 3.
# If CELEB is the word and player guessed ABBEY, B at both the 2nd and 3rd position have state 2.
# If SHARP is the word and player guessed ABBEY, B at both the 2nd and 3rd position have state 1.
# Leaderboard is ascended by the amount of total guesses among all the validation test cases.
# Victory Conditions
# You guess the word in less than 27 turns.
# Defeat Conditions
# You use more than 26 guesses.
# You make a guess which is too short or too long.
# Your guess containing characters other than alphabetical letters.
#  	Note
# It is allowed to make guesses with unreal words although the word the player have to guess is a real word.
#  	Game Input
# The program must first read the initialization data from standard input. Then, provide to the standard output one line for each game turn.
#
# Initialization input
# Line 1: An integer wordCount, number of words in the word set.
#
# Line 2: wordCount amount of space separated words, each containing exactly 6 letters.
# Represents the word set, the word the player have to guess belongs to the word set.
#
# Input for a game turn
# A single line: 6 space separated integers, each representing the state of the letter of the corresponding position of previous guess.
#
# For the first turn all the 6 states are 0.
# Output for a game turn
# A single line containing a word of length 6 letters in uppercase.
# Constraints
# wordCount ≈ 10000
# Word length = 6 letters
# Response time per turn ≤ 50 ms
# Response time for the first turn ≤ 1000 ms
# Number of turns ≤ 26

import sys
# import math
import random

import time

from collections import Counter
from collections import defaultdict

CI = 0
CC = ""


def p(*s):
    # return
    print(*s, file=sys.stderr, flush=True)


WORD_LENGTH = 6
'''length of the word to guess'''

start_time = time.time()  # record the start time


def ptime(msg=''):
    """ad-hoc profiling"""
    global start_time
    end_time = time.time()  # record the end time
    elapsed_time = end_time - start_time  # calculate the elapsed time
    print(msg + " Elapsed time: ", elapsed_time, "seconds\n", flush=True, file=sys.stderr)
    start_time = time.time()


def dict2str(d):
    """convert a guess dictionary d to a string
        where d is a dictionary of {0:'A', 5:'B', 3:'C'}"""
    res = ''
    for i in range(WORD_LENGTH):
        if i in d:
            res += d[i]
        else:
            res += '_'
    return res


word_count = int(input())  # Number of words in the word set
words_string = input()

ptime("Read words")

words_list = words_string.split()
words_set = set(words_list)

ptime("Set of words")

letters_count = Counter(words_string)
del letters_count[' ']

most_common_letters = letters_count.most_common()

p("#Words", len(words_set), word_count)
p("Chars", letters_count)

ptime("most common characters")

free_positions = set(range(WORD_LENGTH))
letter_known = set()
letter_not_in = set()

letter_at_position = {}
'''dict pos -> letter at this position'''
letter_not_at_postion = defaultdict(set)
'''dict pos -> {letters not at this position}'''
guess = {}
'''dict pos -> letter position'''

ptime("Initialization of data for every step")

contains_letter = defaultdict(set)
''' dict char -> set of words that contain this letter'''
for w in words_list:
    for c in w:
        contains_letter[c].add(w)

p(len(contains_letter))

ptime("Sets of words for each letter on any position")

contains_letter_at_pos = defaultdict(set)
''' dict (i, char) -> set of words that contain this letter'''
for w in words_list:
    for i, c in enumerate(w):
        contains_letter_at_pos[(i, c)].add(w)

p(len(contains_letter_at_pos))

ptime("Sets of words for each letter on given position")

freq_letter_at_pos = {(i, c): (len(contains_letter_at_pos[(i, c)])) for i, c in contains_letter_at_pos.keys()}
'''dict (pos, char) -> freq'''
# freq_letter_at_pos.sort(key=lambda x: x[2], reverse=True)
# for i, c in freq_letter_at_pos:
#    p(i, c, freq_letter_at_pos[(i, c)])

most_freq_pos = defaultdict(list)
'''dict char -> List of (pos, freq) sorted by descending frequency'''
for c, pos in most_common_letters:
    for i in range(WORD_LENGTH):
        if contains_letter_at_pos[(i, c)]:
            most_freq_pos[c].append((i, freq_letter_at_pos[(i, c)]))

for c in most_freq_pos.keys():
    most_freq_pos[c] = sorted(most_freq_pos[c], key=lambda x: x[1], reverse=True)
p(most_freq_pos.items())

ptime("Frequencies of each letter on a give position")


def try_data():
    """ try to use data from verifiers, obtained by fixing char C at pos I"""
    verifiers = defaultdict(dict)
    for line in data.splitlines():
        i, c, *s = line.split()
        i = int(i)
        for ver_num in map(int, s):
            verifiers[ver_num][i] = c
    for num in verifiers:
        p("verifier", num, verifiers[num])
        curr_dict = verifiers[num]
        start = tuple(curr_dict.keys())[0]
        curr_set = contains_letter_at_pos[(start, curr_dict[start])]
        for i, c in curr_dict.items():
            curr_set &= contains_letter_at_pos[(i, c)]
        p("Guess for verifier ", num, "Len", len(curr_set), curr_set if len(curr_set) < 5 else '')
    ptime("words from set intersection")


def guess_could_match(guess, only_pos2chk=''):
    """there are words that match the guess, where
        guess is dict pos -> letter at this position """

    for pos, c in guess.items():
        if only_pos2chk != '' and pos != only_pos2chk:
            continue
        if not contains_letter_at_pos[(pos, c)]:
            return False
    return True


# game loop
while True:
    # state: State of the letter of the corresponding position of previous guess
    state = list(map(int, input().split()))

    # analyse the result of the previous guess
    for i in range(WORD_LENGTH):
        if state[i] == 1:
            # letter not in the word
            letter_not_in.add(guess[i])
            words_set -= contains_letter[guess[i]]
        elif state[i] == 2:
            # letter in the word but at different position
            letter_known.add(guess[i])
            letter_not_at_postion[i].add(guess[i])
            words_set -= contains_letter_at_pos[(i, guess[i])]
        elif state[i] == 3:
            # letter it the word exactly at this position
            letter_known.add(guess[i])
            letter_at_position[i] = guess[i]
            words_set &= contains_letter_at_pos[(i, guess[i])]
            if i in free_positions:
                free_positions.remove(i)
        else:
            # impossible situation
            p(state)
            Exception("impossible game input")
    p("#Possible words", len(words_set))
    p(tuple(words_set)[:15])

    guess = {}
    guess_s = ''
    flag_partial_guess = False
    # as long as not all WORD_LENGTH letters are known, keep guessing starting with most common letter
    if most_common_letters and len(letter_known) < WORD_LENGTH:
        flag_partial_guess = True
        while most_common_letters and len(guess) < WORD_LENGTH:
            c, _ = most_common_letters.pop(0)  # take the most common remaining letter
            # check if there are possible words with this letter left
            if any(c in word for word in words_set):
                for i, _ in most_freq_pos[c]:
                    if i in guess.keys():
                        continue
                    guess[i] = c
                    break

    # now construct a good guess
    vacant_this_turn = set()
    use_doubles = len(letter_known) < WORD_LENGTH  # if we have to use a known letter more than once
    letter_to_use = letter_known.copy()

    for i in range(WORD_LENGTH):
        if i not in guess:
            if i in letter_at_position:
                guess[i] = letter_at_position[i]
                if not use_doubles:
                    letter_to_use.remove(guess[i])
            else:
                vacant_this_turn.add(i)
    # print out for debugging
    p("most_common", most_common_letters)
    p("use_doubles", use_doubles)
    p("vacant_this_turn", vacant_this_turn)
    p("guess", guess)
    p("letter_at_position", letter_at_position)
    p("letter_not_at_position", letter_not_at_postion)
    p("letter_known", letter_known)

    while vacant_this_turn:
        vacant_this_turn_copy = vacant_this_turn.copy()
        letter_to_use_copy = letter_to_use.copy()
        p("vacant_this_turn", vacant_this_turn)
        while vacant_this_turn:
            i = vacant_this_turn.pop()
            i_possible = letter_to_use - letter_not_at_postion[i]
            if i_possible:
                guess[i] = random.choice(list(i_possible))
            else:
                guess[i] = random.choice(list(letter_to_use))
            if not use_doubles:
                letter_to_use.remove(guess[i])

        guess_s = dict2str(guess)
        p("generated", guess_s)
        if not flag_partial_guess and guess_s not in words_set:
            vacant_this_turn = vacant_this_turn_copy
            letter_to_use = letter_to_use_copy

    if not guess_s:
        guess_s = dict2str(guess)
        p("guessed", guess_s)

    if not flag_partial_guess and CC:
        guess[CI] = CC
        guess_s = dict2str(guess)
        p("PATCHED", guess_s)

    print(guess_s)

    ptime("Guess")
    # break
    #
    # TTL = 50  # milliseconds
    # TTLs = TTL / 1000
    #
    # import signal
    # import time
    #
    #
    # def bfs_search(start_state, t=TTLs):
    #     stop_flag = False
    #
    #     def interrupt_search(signum, frame):
    #         nonlocal stop_flag
    #         stop_flag = True
    #
    #     signal.signal(signal.SIGALRM, interrupt_search)
    #     signal.setitimer(signal.ITIMER_REAL, t)  # set a 50 ms timer
    #
    #     queue = [(start_state, [])]
    #     best_move = start_state
    #     while queue:
    #         # state, path = queue.pop(0)
    #
    #         # check if we have run out of time
    #         if stop_flag:
    #             break
    #
    #         # do BFS here
    #         best_move += 1
    #         # queue.append((best_move, []))
    #
    #     signal.setitimer(signal.ITIMER_REAL, 0)  # cancel the timer
    #
    #     return best_move  # return the best move found by the search algorithm
    #
    #
    # print(bfs_search(0, 0.05), TTLs)
# letter_known {'N', 'A', 'B'}
# generated WORD6L x 81 times before time-out
