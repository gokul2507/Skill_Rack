l=[list(map(int,input().split())) for _ in range(int(input()))]
x1,y1,x2,y2=map(int,input().split())
c=0
for i,j in l:
    if x1<=i<=x2 and y2<=j<=y1:
        c+=1
print(c)
