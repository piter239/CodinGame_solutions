I = input
n = int(I())
print(sum(6 * (x == 'PASS') + (x == 'PASS' and i == 15) * 4 for i, x in enumerate([I() for _ in range(n)])))
