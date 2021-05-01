def count(z):
    c=0
    for _ in range(2):
        for i in z:
            if len(set(i))==1:
                c+=1
        z=list(zip(*z))
    return c
def findindex(z,a):
    for i in range(5):
        if a in z[i]:
            return i,z[i].index(a)
    return -1,-1
z=[list(map(int,input().split())) for _ in range(5)]
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    r,c=findindex(z,l[i])
    if r!=-1:
        z[r][c]='-'
    if count(z)>=5:
        print(i+1)
        exit()
