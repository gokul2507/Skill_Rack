a=int(input())
z=list(map(int,input().split()))
l=[0 for _ in range(a)]
for i in input().strip():
    s,e,t=0,a-1,1
    if i=='R':
        s,e,t=1,a,-1
        if z[0]:
            z[0]-=1
    else:
        if z[-1]:
            z[-1]-=1
    for j in range(s,e):
        if z[j]:
            l[j+t]+=1
            z[j]-=1
print(*l)