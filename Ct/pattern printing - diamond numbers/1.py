a=int(input())
l=[[0 for _ in range(a+a-1)] for _ in range(a+a-1)]
x,y=0,a-1
t=1
while y>=0:
    l[x][y]=t
    t+=1
    x+=1
    y-=1
y+=2
while x<a+a-1:
    l[x][y]=t
    t+=1
    x+=1
    y+=1
x-=2
while y<a+a-1:
    l[x][y]=t
    t+=1
    y+=1
    x-=1
y-=2
while x:
    l[x][y]=t
    t+=1
    y-=1
    x-=1
for i in l:
    print(*i)
