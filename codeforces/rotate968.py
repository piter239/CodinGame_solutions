# from timeit import default_timer as timer
import random

into = {"6": "9", "8": "8", "9": "6"}


def rotate(s, begin, end):
    """ rotate the string s containing only 6, 8 9 characters
    according to the dict into"""
    r = ''.join([into[c] for c in s[begin:end][::-1]])
    return s[:begin] + r + s[end:]


def generate_string(n):
    """for given n generate string containing n random characters '689' """
    return ''.join(random.choice('689') for _ in range(n))


def generate_case(n):
    """ for given n use generate_string and then rotate it for a random number of times"""
    s = generate_string(n)
    e = s
    count = random.randint(1, n)
    for _ in range(count):
        first, second = random.randint(0, n - 1), random.randint(0, n - 1)
        first, second = min(first, second), max(first, second)
        e = rotate(e, first, second)
    return s, e, count


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
    # print('8', s, f, sep='\n')

    while i < end and s[i:end].count('8'):
        i = s[i:end].index('8') + i
        j = f[j:end].index('8') + j
        assert j < end
        if i != j:
            a, b = min(i, j), max(i, j)
            # special case  must be handled:
            # s = 8868
            # f = 6888
            # here a = 0, b = 1, but after rotating s with s = rotate(s, 0, 1+1) the s would NOT be changed
            if s[a] == '8' == s[b]:
                # now we have to find the first not-8 after index a in s:
                c = a + 1
                while s[c] == '8':
                    c += 1

                s = rotate(s, a, c + 1)
                res += [[a, c]]
            else:
                s = rotate(s, a, b + 1)
                # print('8 '+str(a)+' '+str(b), s, f, sep='\n')
                res += [[a, b]]
        i = j = min(i, j) + 1

    # print('8', s, f, sep='\n')

    for i, c in enumerate(s):
        if s[i] != f[i]:
            res += [[i, i]]
            s = rotate(s, i, i + 1)

    # print('69', s, f, sep='\n')
    assert s == f
    return res


def test(n):
    for _ in range(n):
        s, f, count = generate_case(random.randint(1, 1000))
        print(s, f, count, sep='\n')
        try:
            res = find_rotations(s, f)
            print("DONE", '\n')
        except:
            print("ERROR", '\n')


# test(10)

def test1():
    s = '89988686996696686668666699868666999899889996998989888889686966'
    f = '86689686988888666869999669969989998868696986869699869968898696'
    res = find_rotations(s, f)
    print(res)


# test1()


start = input()
finish = input()

if start == finish:  # just for the case of equal start and finish
    print(0)
    exit()

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
