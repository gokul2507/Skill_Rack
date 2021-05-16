r,c=map(int,input().split())
m=[list(map(str,input().split())) for i in range(r)]
t=int(input())
for i in range(r):
    for j in range(c):
        if m[i][j].isdigit():
            print(m[i][j],end=' ')
        else:
            s=[int(m[k][j]) for k in range(r) if k!=i]
            print(t-sum(s),end=' ')
    print()
