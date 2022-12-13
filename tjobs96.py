n,_,t=open(0)
d=[0]*int(n)
for j in list(map(int,t.split())):d[d.index(min(d))]+=j
print(max(d))