m,n=map(int,input().split())
a=[input().split() for i in range(m)]
r,c=map(int,input().split())
b=[input().split() for i in range(r)]
s,k=1,0
while s<=min(m,n,r,c):
    ac=''
    bc=''
    for i in range(m-s,m):
        for j in range(n-s,n):
            ac+=a[i][j]
    for i in range(r-s,r):
        for j in range(c-s,c):
            bc+=b[i][j]
    if ac==bc:
        k=s
    s+=1
if k==0: 
    print(-1)
    exit()
for i in range(m-k,m):
    for j in range(n-k,n):
        print(a[i][j],end=' ')
    print()