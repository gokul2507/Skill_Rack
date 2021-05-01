def gcd(a,b):
    while a:
        a,b=b%a,a
    return b
input()
z=list(map(int,input().split()))
t=z[0]
for i in z[1:]:
    t=gcd(t,i)
print(t)
