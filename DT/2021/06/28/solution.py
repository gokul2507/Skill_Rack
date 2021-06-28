n=int(input())
z=[int(i) for i in input().split()]
x=int(input())
pre=0
for i in range(n):
    z[-i-1]+=pre
    if z[-i-1]>x:
        pre=z[-i-1]-x
        z[-i-1]=x
    else:
        pre=0
print(*z)