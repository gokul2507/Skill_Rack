import math 
def sq(n):
    s=int(math.sqrt(n))
    return s*s==n 
def fib(n):
    return sq(5*n*n+4) or sq(5*n*n-4) 
input()
for i in list(map(int,input().split())):
    if fib(i):
        print(i,end=' ')