n=int(input())
l=list(map(int,input().split()))
print(l[1],end=' ')
for i in range(1,n-1):
    print(l[i-1]+l[i+1],end=' ')
print(l[-2])
