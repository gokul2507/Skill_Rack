r,c=map(int,input().split())
mat=[]
row=[]
for _ in range(r):
    temp=list(map(int,input().split()))
    row.append(max(temp))
    mat.append(temp)
col=[]
for co in list(zip(*mat)):
    col.append(max(co))
for i in range(r):
    for j in range(c):
        temp=min(row[i],col[j])
        if mat[i][j]==0:
            temp=0
        print(temp,end=' ')
    print()
