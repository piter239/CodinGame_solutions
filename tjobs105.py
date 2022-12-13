n,_,t = open(0)
d=[0]*int(n)
for j in list(map(int,t.split())):
 w=min(d)
 d[d.index(w)]+=j
print(max(d))