def swap(s: str, i: int) -> str:
    res = list(s)
    assert 0 <= i < len(s) - 2, "i must be between 0 and len(s) - 2"
    for j in range(i, i + 3):
        res[j] = {"X": ".", ".": "X"}[res[j]]
    return ''.join(res)


def min_number_of_swaps(s: str) -> int:
    # linear algorithm - I have no proof of optimality yet
    swaps = 0
    visited = set()
    visited.add(s)
    # print(visited)
    i = 0
    while i < len(s) - 2:
        if s[i] == ".":
            s = swap(s, i)
            visited.add(s)
            swaps += 1
        i += 1
    if s != "X" * len(s):
        return -1
    else:
        return swaps


# print('X.XX.',min_number_of_swaps('X.XX.'))
# print('XXXXXX',min_number_of_swaps('XXXXXX'))
# print('X.X.',min_number_of_swaps('X.X.'))
# print('X.X.X',min_number_of_swaps('X.X.X'))
# print('X.X.X.X',min_number_of_swaps('X.X.X.X'))
# print('X.X.X.',min_number_of_swaps('X.X.X.'))

input()
print(min_number_of_swaps(input()))
