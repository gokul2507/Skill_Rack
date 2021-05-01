x,y=map(int,input().split())
p,q=map(int,input().split())
a=[[0]*8 for i in range(8)]
x-=1;y-=1;p-=1;q-=1
a[x][y]='Q'
a[p][q]='K'
for i in range(8):
    for j in range(8):
        if (i,j)==(x,y) or (i,j)==(p,q):
            continue
        if i==x or j==y or i+j==x+y or i-j==x-y:
            a[i][j]='q'
d=[[-2,-1],[-2,1],[2,-1],[2,1],[-1,2],[-1,-2],[1,2],[1,-2]]
for dx,dy in d:
    i,j=p+dx,q+dy 
    if 0<=i<8 and 0<=j<8 and a[i][j]!='Q':
        a[i][j]=('x' if a[i][j]=='q' else 'k')
for i in a:
    print(*i)
