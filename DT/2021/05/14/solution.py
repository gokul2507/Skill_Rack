def change(x):
    a,n=[],[]
    for i in x:
        if i.isalpha():
            a.append(i)
        else:
            n.append(i)
    return a+n
q,w=map(int,input().split())
z=list(zip(*[input().split() for _ in range(q)]))
for i in range(w):
    z[i]=change(list(z[i]))
for i in list(zip(*z)):
    print(*i)