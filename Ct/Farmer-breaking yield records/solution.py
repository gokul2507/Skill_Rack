n,b,d=int(input()),[],[]
v=[int(i) for i in input().split()]
c,e=v[0],v[0]
for i in v:
    if i>e:
        b.append(i)
        e=i
    if i<c:
        d.append(i)
        c=i
print(len(b),len(d))
