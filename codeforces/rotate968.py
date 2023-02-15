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


def find_rotations(s, f, begin, end):
    """ for strings s, f
    return a list of pairs within [begin:end]
    such that rotations of substrings from s for each pair results in f (considered from begin to end)
    pairs are considered 0-indexed positions in s
    empty list means no possible rotations found.
    Always: end > begin"""
    assert end > begin
    if len(s) != len(f):
        return []
    if s[begin:end].count('8') != f[begin:end].count('8'):
        return []

    if s[begin:end] == f[begin:end]:
        return [[begin, end], [begin, end]]

    if rotate(s[begin:end], 0, end - begin) == f[begin:end]:
        return [[begin, end]]

    matching_substrings = []
    i = begin
    while i < end:
        j = i
        while s[j] == f[j] and j < end:
            j += 1
            if j == end:
                break
        if j > i:
            matching_substrings.append((i, j))
            i = j
        else:
            i += 1
    # print(matching_substrings)

    if not matching_substrings:
        return []

    for a, b in matching_substrings:
        if begin == a:
            r2 = [find_rotations(s, f, b, end)]
            if all(r2):
                return r2[0]
            r3 = [find_rotations(s, f, a, end)]
            if all(r3):
                return r3[0]

        elif end == b:
            r1 = [find_rotations(s, f, begin, a)]
            if all(r1):
                return r1[0]
            r2 = [find_rotations(s, f, begin, b)]
            if all(r2):
                return r2[0]

        else:
            r1 = [find_rotations(s, f, begin, a), find_rotations(s, f, b, end)]
            if all(r1):
                return r1[0] + r1[1]
            r2 = [find_rotations(s, f, begin, b), find_rotations(s, f, b, end)]
            if all(r2):
                return r2[0] + r2[1]
            r3 = [find_rotations(s, f, begin, a), find_rotations(s, f, a, end)]
            if all(r3):
                return r3[0] + r3[1]
    return []


# print(rotate(s, 0, len(s)-1))

res = find_rotations(start, finish, 0, len(start))

if res:
    print(len(res))
    for p in res:
        print(p[0] + 1, p[1])
else:
    print(-1)

"""
# 98 699 99
# 98 66 669
# 99 86 669
# 699 98 66

test1
9869999
6999866

9869999
9866669

9866669
9986669

9986669
6999866

# 9 99
  9669899
# 6999866


"""
