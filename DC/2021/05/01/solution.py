x,y=map(int,input().split())
for k in range(y):
    z=[]
    for i in range(y):
        z.append(list(list((i+k)%2 for _ in range(x)) for _ in range(x)))
    t=list(zip(*z))
    for i in t:
        for j in i:
            print(*j,end=' ')
        print()