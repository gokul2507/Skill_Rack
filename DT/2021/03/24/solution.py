r,c=map(int,input().split())
z=[]
q=[]
for i in range(r):
    l=input().split()
    for j in range(c):
        if l[j].isalpha():
            q.append((i,j))
    z.append(l)
for i,j in q:
    z[i-1][j],z[i][j-1]=z[i][j-1],z[i-1][j]
    z[i-1][j+1],z[i+1][j-1]=z[i+1][j-1],z[i-1][j+1]
    z[i][j+1],z[i+1][j]=z[i+1][j],z[i][j+1]
for i in z:
    print(*i)
