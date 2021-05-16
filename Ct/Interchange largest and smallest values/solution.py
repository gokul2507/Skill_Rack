a=int(input())
b=list(map(int,input().split()))
for i in b:
    if i==max(b):print(min(b),end=' ')
    elif i==min(b):print(max(b),end=' ')
    else:print(i,end=' ')
