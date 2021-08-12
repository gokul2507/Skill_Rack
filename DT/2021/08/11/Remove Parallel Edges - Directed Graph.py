n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
t=[]
for i in range(n):
    for j in range(n):
        if l[i][j]!=0 and l[j][i]!=0:
            if l[i][j]>l[j][i]:
                l[i][j]=0
            else:
                l[j][i]=0
for i in l:
    print(*i)