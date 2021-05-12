r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
n,t=map(int,input().split())
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i==r-1 or j==c-1:
            m[i][j]+=(n*2)*t 
        else:m[i][j]+=(n*t) 
for i in m:
    print(*i)
