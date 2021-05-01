x,y=map(int,input().split())
z=[input().split() for _ in range(x)]
def submat(r1,c1,r2,c2,s):
    for i in range(r1,r2):
        for j in range(c1,c2):
            if z[i][j]!='0':
                s=s.upper()
            else:
                s=s.lower()
            z[i][j]=s
k=int(input())
l="abcdefghijklmnopqrstuvwxyz"
li=0
for i in range(x-k,-1,-k):
    j=0
    while i<x and j<y:
        submat(i,j,i+k,j+k,l[li])
        li+=1
        li%=26
        i+=k
        j+=k
for j in range(k,y,k):
    i=0
    while i<x and j<y:
        submat(i,j,i+k,j+k,l[li])
        li+=1
        li%=26
        i+=k
        j+=k
for i in z:
    print(*i)
