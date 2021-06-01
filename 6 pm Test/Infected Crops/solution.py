a,b=map(int,input().split())
z=[]
l=[]
for i in range(a):
    k=list(input().strip().split())
    for j in range(b):
        if k[j]=="I":
            l.append((i,j))
    z.append(k)
while l:
    i=l.pop(0)
    x,y=i[0],i[1]
    z[x][y]="D"
    if x+1<a and z[x+1][y] not in "GD":
        z[x+1][y]="D"
        l.append((x+1,y))
    if x-1>=0 and z[x-1][y] not in "GD":
        z[x-1][y]="D"
        l.append((x-1,y))
    if y+1<b and z[x][y+1] not in "GD":
        z[x][y+1]="D"
        l.append((x,y+1))
    if y-1>=0 and z[x][y-1] not in "GD":
        z[x][y-1]="D"
        l.append((x,y-1))
for i in z:
    print(*i)