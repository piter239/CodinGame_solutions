n, s = 2, 4
b, m = s * '*', '*' + ' ' * (s - 2) + '*'
for r in zip(*[[b] + [m] * (s - 2) + [b]] * n): print(*r, sep='')
print(*zip(*[[b] + [m] * (s - 2) + [b]] * n))
print(*[[b] + [m] * (s - 2) + [b]] * n)
