from math import gcd
input()
l=list(map(int,input().split()))
x=l[0]
for i in l[1:]:
    x=gcd(x,i) 
print(x)