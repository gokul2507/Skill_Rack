a=int(input())
def g():
    return list(list(map(int,input().split())) for _ in range(a))
m1=g()
m2=g()
def get(z):
    l=[]
    while z:
        t=list(z[0])
        z=z[1:]
        if z:
            t+=list(z[-1])
            z=z[:-1]
        if z:
            z=list(zip(*z))
            t+=list(z[0])+list(z[-1])
            z=z[1:-1]
        l.append(t)
    return l
ml1=get(m1)
ml2=get(m2)
s=0
f=1
for i,j in zip(ml1[::-1],ml2[::-1]):
    if i==j:
        s+=sum(j)
        f=0
    else:
        break
if f:
    s=-1
print(s)