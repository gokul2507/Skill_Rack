r,c=map(int,input().split())
z=[input().split() for _ in range(r)]
k=int(input())
def change(r1,c1,r2,c2):
    for i in range(c1,c2+1):
        x,y=r1,r2
        while x<y:
            z[x][i],z[y][i]=z[y][i],z[x][i]
            x+=1
            y-=1
for i in range(0,r,k):
    for j in range(0,c,k):
        if z[i+k-1][j+k-1].lower() in "aeiou":
            change(i,j,i+k-1,j+k-1)
for i in z:
    print(*i)
