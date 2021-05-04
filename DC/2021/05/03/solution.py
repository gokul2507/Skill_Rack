r,c=map(int,input().split())
z=[input().split() for _ in range(r)]
def sort(x,y):
    l=1
    for i in range(x,x+3):
        for j in range(y,y+3):
            z[i][j]=l
            l+=1
def contain(x,y):
    l=set()
    for i in range(x,x+3):
        for j in range(y,y+3):
            l.add(z[i][j])
    if len(l)<9:
        return
    sort(x,y)
for i in range(0,r,3):
    for j in range(0,c,3):
        contain(i,j)
for i in z:
    print(*i)