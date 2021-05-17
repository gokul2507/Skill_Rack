from math import factorial
t,n=[int(i) for i in input().split()]
r=t+n-1
r1,r2,r3=factorial(r),factorial(t),factorial(r-t)
print((r1//(r2*r3))%1000000007)