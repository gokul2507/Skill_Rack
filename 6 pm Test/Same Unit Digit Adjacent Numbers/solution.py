def check(n,x,y):
    if y==0:
        return m[x][y+1]%10==n
    if y==c-1:
        return m[x][y-1]%10==n
    return m[x][y-1]%10==n or m[x][y+1]%10==n
r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
count=0 
if c==1:
    print(0)
    exit()
for i in range(r):
    for j in range(c):
        count+=check(m[i][j]%10,i,j)
print(count)