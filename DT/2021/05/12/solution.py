a,b=map(int,input().split())
z=[input().split() for _ in range(a)]
s=input().strip()
def replace(x,y):
    global s
    while s:
        z[x][y]=s[0]
        s=s[1:]
        y+=1
        x+=y//b
        y%=b
        x%=a
    for i in z:
        print(*i)
for i in range(a):
    for j in range(b):
        if z[i][j]==s[0]:
            replace(i,j)
            exit()