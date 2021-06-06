l=list(map(int,input().split()))
for i in sorted(set(l))[::-1]:
    print(i,l.count(i))