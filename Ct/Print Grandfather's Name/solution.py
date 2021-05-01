x=input().split()
y=input().split()
z=input().split()
if y[1] not in [x[0],z[0]]:
    x=y
elif z[1] not in [x[0],y[0]]:
    x=z
print(*x)
