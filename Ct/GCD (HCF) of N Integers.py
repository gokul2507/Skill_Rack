from math import gcd
a=int(input())
l=list(map(int,input().split()))
n=l[0]
for i in l[1:]:
    n=gcd(n,i)
print(n)
