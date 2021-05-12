ans=0
def check(z,r,c,i,j):
    global ans
    if not 0<=i<r or not 0<=j<c:
        return
    if z[i][j]=='|':
        return
    if i==r-1 and j==c-1:
        ans+=1
    check(z,r,c,i,j+1)
    check(z,r,c,i+1,j)
a,b=map(int,input().split())
z=[list(map(str,input().split())) for _ in range(a)]
check(z,a,b,0,0)
print(ans)
