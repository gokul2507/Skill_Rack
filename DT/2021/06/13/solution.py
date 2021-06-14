x,y=map(int,input().split())
z=[input().split() for _ in range(x)]
a,b=map(int,input().split())
t=z[a-1][b-1]
l=int(len(t)**0.5)
for _ in range(l):
    print(t[:l])
    t=t[l:]