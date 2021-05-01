a,b=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(a)]
z=[]
for i in range(a-1):
    if i==0 or i==a-2:
        for j in range(b-1):
            z.append(l[i][j:j+2]+l[i+1][j:j+2])
    else:
        z.append(l[i][:2]+l[i+1][:2])
        z.append(l[i][-2:]+l[i+1][-2:])
z=sorted(z,key=lambda i:sum(i),reverse=1)
print(*z[0][:2])
print(*z[0][2:])
