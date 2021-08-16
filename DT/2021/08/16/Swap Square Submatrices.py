r,c,x=map(int,input().split())
z=[input().split() for _ in range(r)]
r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
r1-=1+(x//2)
r2-=1+(x//2)
c1-=1+(x//2)
c2-=1+(x//2)
for i in range(x):
    for j in range(x):
        z[r1+i][c1+j],z[r2+i][c2+j]=z[r2+i][c2+j],z[r1+i][c1+j]
for i in z:
    print(*i)