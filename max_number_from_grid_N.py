# CoC
# https://www.codingame.com/clashofcode/clash/report/28635931bad85d0dc16bcabf3849a5cfad63b52
# find the biggest number that can be build from a grid N * N starting on given position and
# taking N number, wrapping around if necessary.
test_case_10 = '''10
2391862821
9037983536
2139839392
5896672665
3008877263
5959600631
2242106277
1254567628
6191759746
7689475927

correct answer
9895450933
'''

test_3 = '''3
123
456
789
'''

import sys

n = int(input())
r = []
for i in range(n):
    r.append(input())

tw = []

for i in range(n):
    d = ''
    for j in range(n):
        d += r[j][i]
    r.append(d)

rr = r + [c[::-1] for c in r]

w = []
for c in rr:
    w.append(c)
    for i in range(1, n):
        w.append(c[i:] + c[:i])

ww = [int(''.join(c)) for c in w]

print(len(w), sorted(w), file=sys.stderr)

print(max(ww))
