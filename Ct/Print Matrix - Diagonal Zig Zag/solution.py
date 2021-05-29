a,b=map(int,input().split())
z=[input().split() for _ in range(a)]
c=True
for j in range(b):
    i=0
    l=[]
    while 0<=i<a and 0<=j<b:
        l.append(z[i][j])
        i+=1
        j-=1
    if c:
        l=l[::-1]
    print(*l,end=' ')
    c=not c
for i in range(1,a):
    j=b-1
    l=[]
    while 0<=i<a and 0<=j<b:
        l.append(z[i][j])
        i+=1
        j-=1
    if c:
        l=l[::-1]
    print(*l,end=' ')
    c=not c