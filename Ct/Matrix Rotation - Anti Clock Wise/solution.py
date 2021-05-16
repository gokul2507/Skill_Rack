r,c,o=map(int,input().split())
z=[input().split() for _ in range(r)]
def make(i,j):
    if t:
        l.append(z[i][j])
    else:
        z[i][j]=l.pop(0)
def getandfix():
    for i in range(k,c-k):
        make(k,i)
    for i in range(k+1,r-k):
        make(i,c-k-1)
    for i in range(c-k-2,k-1,-1):
        make(r-k-1,i)
    for i in range(r-k-2,k,-1):
        make(i,k)
for k in range(0,(min(r,c)+1)//2):
    t,l=1,[]
    getandfix()
    x=o%len(l)
    l,t=l[x:]+l[:x],0
    getandfix()
for i in z:
    print(*i)
