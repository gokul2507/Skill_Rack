n=int(input())
for i in list(zip(range(1,n//2+1),range(n,n//2,-1))):
    print(*i,end=' ')
if n%2:print(n//2+1)
