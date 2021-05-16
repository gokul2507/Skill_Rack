r,c=map(int,input().split())
m=[input().split() for i in range(r)]
for i in range(r):
    for j in range(c):
        if m[i][j]=='B':
            m[i][j]='-' 
m=[sorted(i) for i in list(zip(*m))]
m=list(zip(*m))
for i in m:
    print(*i)
