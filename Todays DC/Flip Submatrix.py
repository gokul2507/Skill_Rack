import copy
r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
z=copy.deepcopy(m)
x,y,k=map(int,input().split())
x,y=x-1,y-1
for i,i1 in zip(range(x,x+k),range(x+k-1,x-1,-1)):
    for j in range(y,y+k):
        m[i][j]=z[i1][j]
for i in m:
    print(*i)