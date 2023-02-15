start = input()
finish = input()

into = {"6": "9", "8": "8", "9": "6"}

if start == finish:  # just for the case of equal start and finish
    print(0)
    exit()


def rotate(s, begin, end):
    """ rotate the string s containing only 6, 8 9 characters
    according to the dict into"""
    r = ''.join([into[c] for c in s[begin:end][::-1]])
    return s[:begin] + r + s[end:]


def find_rotations(s, f):
    """ for strings s, f
    return a list of pairs
    such that rotations of substrings from s for each pair results in f
    pairs are considered 0-indexed positions in s
    empty list means no possible rotations found."""

    if len(s) != len(f):
        return []
    if s.count('8') != f.count('8'):
        return []
    begin = 0
    end = len(s)

    # no-recursion approach: bring all 8's onto the same position in both strings,
    # then just rotate the remaining unequal substrings of the length 1
    res = []
    i = j = begin
    while i < end and s[i:end].count('8'):
        i = s[i:end].index('8') + i
        j = f[j:end].index('8') + j
        assert j < end
        if i != j:
            a, b = min(i, j), max(i, j)
            f = rotate(f, a, b + 1)
            res += [[a, b]]
        i = j = min(i, j) + 1

    for i, c in enumerate(s):
        if s[i] != f[i]:
            res += [[i, i]]
            f = rotate(f, i, i + 1)

    assert s == f
    return res


result = find_rotations(start, finish)

if result:
    print(len(result))
    for p in result:
        print(p[0] + 1, p[1] + 1)
else:
    print(-1)

"""
test1
9869999
6999866

test2
988686
968988
"""
