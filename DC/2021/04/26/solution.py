r,c=map(int,input().split())
m=[input().split() for i in range(r)]
for i in range(c):m[0][i]='x'
for i in range(c):
    for j in range(1,r):
        if m[j][i]=='=':break
        elif m[j][i]=='-':m[j][i]='x' 
for i in m:
    print(*i)
