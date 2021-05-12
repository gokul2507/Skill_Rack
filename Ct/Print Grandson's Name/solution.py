a,b,c=[input().split() for i in range(3)]
if b[0] not in [a[1],c[1]]:
    a=b
elif c[0] not in [a[1],b[1]]:
    a=c 
print(*a)
