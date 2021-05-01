a=int(input())
l=list(map(int,input().split()))
t=int(input())
while t:
    t-=1
    x=l.pop(0)
    if x%2:
        l+=list(range(1,x+1))
    else:
        l+=list(range(x//2,0,-1))
print(len(l))
