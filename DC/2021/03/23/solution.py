n=int(input())
l=list(map(int,input().split()))
r,f=1,1
for i in l:
    if i-r!=0:
        print(r,i-1,sep='-',end=' ')
        f=0 
    r=i+1 
if f:print(-1)
