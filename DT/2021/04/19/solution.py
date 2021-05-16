n=int(input())
z=[list(map(int,input().split())) for _ in range(n)]
k=int(input())
l=[]
for i in range(0,n,k):
    for j in range(0,n,k):
        t=[]
        for r in range(i,i+k):
            t.append(z[r][j:j+k])
        l.append(t)
l.sort(key=lambda i:-sum(sum(j) for j in i))
for i in range(0,len(l),n//k):
    for j in list(zip(*l[i:i+n//k])):
        for m in j:
            print(*m,end=' ')
        print()
