r,c,t=map(int,input().split())
z=[input().split() for _ in range(r)]
l=list(map(int,input().split()))
z=list(zip(*z))
for i in range(1,t+1):
    for j in range(c):
        z[j]=list(z[j])
        if i%l[j]==0:
            z[j]=z[j][-1:]+z[j][:-1]
for j in zip(*z):
    print(*j)