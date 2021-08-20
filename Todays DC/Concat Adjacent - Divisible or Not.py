n=int(input())
l=list(map(int,input().split()))
x,f=int(input()),1
for i in range(n-1):
    if int(str(l[i])+str(l[i+1]))%x==0:
        print(l[i],l[i+1])
        f=0
    elif int(str(l[i+1])+str(l[i]))%x==0:
        print(l[i+1],l[i])
        f=0
if f:print(-1)