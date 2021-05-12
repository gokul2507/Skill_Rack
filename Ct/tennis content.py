a=int(input())
d={}
for i in range(a):
    q=input().split()
    d[q[0]]=q[1]
z={}
for i in range(a-1):
    q=input().strip().split("vs")
    if q[0] not in z:
        z[q[0]]=[]
    z[q[0]].append(d[q[1]])
    t=q[0]
print(*z[t][::-1],sep='\n')
