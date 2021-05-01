x,y=map(int,input().split())
z=[list(map(int,input().split())) for _ in range(x)]
for i in range(0,y-(y%2),2):
    t=z[0][i]%10
    l=[z[0][i]]
    for j in range(x):
        if t==z[j][i+1]%10:
            l.append(z[j][i+1])
    for j in range(x-1,0,-1):
        if t==z[j][i]%10:
            l.append(z[j][i])
    l=l[-1:]+l[:-1]
    z[0][i]=l.pop(0)
    for j in range(x):
        if t==z[j][i+1]%10:
            z[j][i+1]=l.pop(0)
    for j in range(x-1,0,-1):
        if t==z[j][i]%10:
            z[j][i]=l.pop(0)
for i in z:
    print(*i)
