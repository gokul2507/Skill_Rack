a,s=map(int,input().split())
for i in range(a):
    l=list(range(s,s+a))
    s+=a
    if i%2:
        l=l[::-1]
    print(*l)
