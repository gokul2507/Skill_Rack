from math import gcd 
r,c=map(int,input().split())
m1=[list(map(int,input().split())) for i in range(r)]
a,b=map(int,input().split())
m2=[list(map(int,input().split())) for i in range(a)]
for i in range(min(r,a)):
    for j in range(min(c,b)):
        print(gcd(m1[i][j],m2[i][j]),end=' ')
    print()
