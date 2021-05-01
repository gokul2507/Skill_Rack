n,x=map(int,input().split())
input()
r=sum(list(map(int,input().split())))
c=0
if r>=n:
    r-=n
    c=1
if r>x or c==0:
    print("HARE")
elif r<x:
    print("TORTOISE")
else:
    print("-1")
