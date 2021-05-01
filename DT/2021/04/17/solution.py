x,y=map(int,input().split())
z1=[list(map(int,input().split())) for _ in range(x)]
z2=list(zip(*list(list(map(int,input().split())) for _ in range(x))))
for i in range(x):
    for j in range(y):
        print(min(min(z1[i]),min(z2[j])),end=' ')
    print()
