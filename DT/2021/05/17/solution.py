x,y=map(int,input().split())
z=[list(map(int,input().split())) for _ in range(x)]
p=int(input())
z,t=z[:p][::-1],z[p:]
if len(z)>len(t):
    t,z=z,t
for i in range(min(len(z),len(t))):
    for j in range(y):
        t[i][j]+=z[i][j]
for i in t:
    print(*i)