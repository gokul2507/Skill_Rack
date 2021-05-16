r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
s,ma=0,max(m[0])
for i in m:
    if ma<max(i):
        ma=max(i) 
for i in range(r):
    for j in range(c):
        if m[i][j]==1:
            x,y=i,j 
for i in range(2,ma+1):
    for row in range(r):
        for col in range(c):
            if m[row][col]==i:
                s+=(abs(x-row)+abs(y-col)) 
                x,y=row,col 
print(s)
