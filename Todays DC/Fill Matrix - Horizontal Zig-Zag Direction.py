n=int(input())
z=list(map(int,input().split()))
r,c=map(int,input().split())
mat=[[0 for i in range(c)] for i in range(r)]
ctr=-1 
x,y=r-1,c-1 
while z:
    mat[x][y]=z.pop(0) 
    y+=ctr 
    if y==-1:
        y=0 
        x-=1 
        ctr*=-1 
    elif y==c:
        y=c-1 
        x-=1 
        ctr*=-1 
    if x==-1:
        x,y,ctr=r-1,c-1,-1 
for i in mat: print(*i)