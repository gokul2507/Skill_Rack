x,y=map(int,input().split())
z=[input().split() for _ in range(x)]
l=[input().split() for _ in range(x)]
for i in range(x):
    for j in range(y):
        if l[i][j].lower() in "aeuio":
            z[i][j],l[i][j]=l[i][j],z[i][j]
        print(z[i][j],end=' ')
    print()
for i in l:
    print(*i)