n,a=int(input()),[int(x) for x in input().split()]
x,y=a[0],max(a[0],a[1])
for i in range(2,n):
    m=max(a[i]+x,y)
    x=y
    y=m
print(m)
