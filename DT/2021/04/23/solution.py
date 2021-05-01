a=int(input())
z=list(map(int,input().split()))
if a>1 and z[0]>z[1]:
    z=z[::-1]
    a=0
t=z[0]
p=t
q=[]
for i in z[1:]:
    if p+1!=i:
        q.append("%d-%d"%(t,p))
        t=i
    p=i
q.append("%d-%d"%(t,p))
if a==0:
    q=q[::-1]
print(*q)
