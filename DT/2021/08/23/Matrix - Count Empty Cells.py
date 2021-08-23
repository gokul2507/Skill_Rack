r,c=map(int,input().split())
n=int(input())
m=[[0 for i in range(c)] for i in range(r)]
for t in range(n):
    count=0
    x,y=map(int,input().split())
    x,y=x-1,y-1
    for i in range(r):
        m[i][y]=1 
    m[x]=[1 for i in range(c)]
    for i in m:
        count+=i.count(0) 
    print(count)