x,y=map(int,input().split())
z=[input().split() for _ in range(x-1)]
a1=input().split()
a2=input().split()
n=list(set(a1)-(set(a1)-set(a2)))[0]
q=a1.index(n)
a1.remove(n)
z.insert(a2.index(n),a1)
z=list(zip(*z))
z.insert(q,a2)
for i in list(zip(*z)):
    print(*i)
