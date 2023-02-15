def min_swaps_to_palindrome(s):
    n = len(s)
    swaps = 0
    s = list(s)
    for i in range(n // 2):
        j = n - 1 - i
        if s[i] != s[j]:
            k = j
            while k > i and s[k] != s[i]:
                k -= 1
            if k == i:
                return -1
            while k < j:
                s[k], s[k + 1] = s[k + 1], s[k]
                swaps += 1
                k += 1
    return swaps


assert min_swaps_to_palindrome("abba") == 0
assert min_swaps_to_palindrome("aabaabb") == 4
assert min_swaps_to_palindrome("ab") == -1
assert min_swaps_to_palindrome("aaaabbbb") == 8

string = input()
print(min_swaps_to_palindrome(string))
