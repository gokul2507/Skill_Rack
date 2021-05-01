a,b,c,d=input().split()
n=int(input())
def pri(x,y):
    print(x*y,end='')
for i in range(n):
    pri("*",i)
    pri(d+" ",n-i)
    pri(a+" ",i+1)
    pri(b+" ",n-i-1)
    print(end=b)
    pri("*",i)
    print()
for i in range(n):
    pri("*",n+1+i)
    pri(c+" ",n-i-1)
    print(end=c)
    pri("*",n+1+i)
    print()