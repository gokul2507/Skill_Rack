row,col,n=map(int,input().split())
arr=list(map(int,input().split()))
x,y=0,0
mat=[[0 for i in range(col)] for j in range(row)]
for i in range(n):
    while arr[i]:
        arr[i]-=1
        mat[x][y]=i+1
        y+=1
        x+=y//col
        y%=col
for ele in mat[::-1]:
    print(*ele)
