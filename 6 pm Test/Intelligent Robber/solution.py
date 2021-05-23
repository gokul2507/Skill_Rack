n,a=int(input()),[int(i) for i in input().split()]
x,y,z=a[0],max(a[0],a[1]),max(a[0],a[1],a[2])
for i in range(3,n):
    t=max(x+a[i],y,z)
    x=y
    y=z
    z=t
print(t)