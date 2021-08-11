r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
m=list(zip(*m))
for i in range(c):
    m[i]=sorted(m[i])
for i in list(zip(*sorted(m,key=lambda i:i.count(0)))):
    print(*i)