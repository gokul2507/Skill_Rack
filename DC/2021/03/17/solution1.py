def check(n,m):
    return 0<=n<x and 0<=m<y and z[n][m]=='*'
x,y=map(int,input().split())
z=[input().split() for _ in range(x)]
c=0
for i in range(x):
    for j in range(y):
        if z[i][j]=='-' and (check(i-1,j-1) or check(i-1,j+1) or check(i+1,j-1) or check(i+1,j+1)):
            c+=1
print(c)
