r,c=map(int,input().split())
l=[input().strip() for i in range(c)]
x=int(input())
for i in range(x):
    l.remove(input().strip())
for i in range(r):
    if i<r and i<len(l):
        print(*l[i],sep='')
