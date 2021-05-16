r,c=map(int,input().split())
l=[input().split()+["-1"] for _ in range(r)]
x,y,z=input().split()
c+=1
tx,ty=int(x)-1,int(y)-1
x,y=tx,ty
p=l[x][y]
while x<r and y<c-1:
    inc=1
    if y%2:
        inc=-1
    x+=inc
    if not 0<=x<r:
        x-=inc
        y+=1
    l[x][y],p=p,l[x][y]
l[tx][ty]=z
for i in l:
    print(*i)