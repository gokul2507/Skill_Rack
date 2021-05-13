inc=1
a=int(input())
l,r=1,(a-1)*4
x,y=a-1,a-1
for i in range(a+a-1):
    z=["0" for _ in range(a+a-1)]
    if x==y:
        z[x]=l
    else:
        z[x],z[y]=l,r
        r-=1
    l+=1
    x-=inc
    y+=inc
    if x==0:
        inc=-1
    print(z)
