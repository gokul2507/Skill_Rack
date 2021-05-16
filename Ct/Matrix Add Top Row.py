a,b=map(int,input().split())
z=[list(map(int,input().split())) for _ in range(a)]
print(*z[0])
for i in range(1,a):
    for q,j in enumerate(z[i]):
        print(j+(z[0][q]//(a-1)),end=' ')
    print(
