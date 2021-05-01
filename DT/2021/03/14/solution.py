x,y=map(int,input().split())
z=[input().split() for _ in range(x)]
k=z[-1][-1][-1]
l=[]
def check(q=0):
    for i in range(y):
        if z[0][i][-1]==k:
            if q:
                z[0][i]=l.pop(0)
            else:
                l.append(z[0][i])
    for i in range(1,x):
        if z[i][-1][-1]==k:
            if q:
                z[i][-1]=l.pop(0)
            else:
                l.append(z[i][-1])
    for i in range(y-2,-1,-1):
        if z[x-1][i][-1]==k:
            if q:
                z[x-1][i]=l.pop(0)
            else:
                l.append(z[x-1][i])
    for i in range(x-2,0,-1):
        if z[i][0][-1]==k:
            if q:
                z[i][0]=l.pop(0)
            else:
                l.append(z[i][0])
check()
l=l[-1:]+l[:-1]
check(1)
for i in z:
    print(*i)
