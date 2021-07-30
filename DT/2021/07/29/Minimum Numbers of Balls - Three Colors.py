n=int(input())
l=[list(map(int,input().strip().split()))for i in range(n)]
for i in range(1,n):
    l[i][0]+=min(l[i-1][1],l[i-1][2])
    l[i][1]+=min(l[i-1][0],l[i-1][2])
    l[i][2]+=min(l[i-1][0],l[i-1][1])
print(min(l[-1]))