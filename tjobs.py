I=input
n=int(I())
I()
d=[0]*n
for j in list(map(int,I().split())):
 w=min(d)
 d[d.index(w)]+=j
print(max(d))
