a,b=map(int,input().split())
z=[list(map(int,input().split())) for _ in range(a)]
d=int(input())
p=[]
l=-1
for i in range(2,a):
    for j in range(b-2):
        if z[i][j+2]%10==d:
            t=[]
            for r in range(i-2,i+1):
                for c in range(j,j+3):
                    t.append(z[r][c])
            if sum(t)>l:
                l=sum(t)
                p=t
if not p:
    print(-1)
    exit()
print(*p[:3])
print(*p[3:6])
print(*p[6:])
