n=int(input())
l=list(map(int,input().split()))
o=sorted([i for i in l if i%2!=0])
e=sorted([i for i in l if i%2==0])
for i in l:
    if i%2:print(o.pop(0),end=' ')
    else: print(e.pop(0),end=' ')
