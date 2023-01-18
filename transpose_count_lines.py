# shortest CoC in Python https://www.codingame.com/clashofcode/clash/report/2855600ec2cade7f89f174ff246ec9bf37b2b38
test = '''
.........
..#......
..###....
..#.#....
..###....
....#....
.........
.........
.........
'''
result = 4

# my solution 118 characters, or 84 characters if shortened
# d=list(open(0))
# d+=[*map(''.join,zip(*d))]
# r=0
# for w in d:r+=sum(1<len(c)for c in w.replace('.',' ').split())
# print(r)

# assert result == r

# best solution 101 characters
# import re
# a=[*open(0)]
# print(a)
# print(sum(len(re.findall('##+',r))for a in[a,map(''.join,zip(*a))]for r in a))


# improve my solution with better input - 114 characters
d = [*open(0)]
r = 0
for w in d + [*map(''.join, zip(*d))]: r += sum(1 < len(c) for c in w.replace('.', ' ').split())
print(r)

# best COMMON solution 94 characters, or 72 characters if shortened
import re

d = [*open(0)]
print(sum(len(re.findall('##+', r)) for r in d + [*map(''.join, zip(*d))]))
