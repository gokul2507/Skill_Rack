n=int(input())
l=list(map(int,input().split()))
for i in range(1,n):
    if l[i]&l[i-1]!=l[i-1]:
        print("NO")
        exit()
print("YES")