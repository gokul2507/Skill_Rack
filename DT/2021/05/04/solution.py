a,b=map(int,input().split())
z=[input().split() for _ in range(a)]
k=int(input())
for i in range(a-k+1):
    for j in range(b-k+1):
        l=[]
        for r in range(i,i+k):
            for c in range(j,j+k):
                l.append(z[r][c])
        if l==sorted(l):
            print("YES")
            exit()
print("NO")