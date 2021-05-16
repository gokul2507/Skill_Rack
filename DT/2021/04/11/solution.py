a,b=map(int,input().split())
z1=[list(map(int,input().split())) for _ in range(a)]
z2=[list(map(int,input().split())) for _ in range(a)]
if z2[0] in z1:
    x=z1.index(z2[0])
    for i in range(x):
        print(*z1[i])
    for i in range(x,a):
        for q,w in list(zip(z1[i],z2[i-x])):
            print(q+w,end=' ')
        print()
    x=a-x
    for i in range(x,a):
        print(*z2[i])
else:
    x=z1.index(z2[-1])
    for i in range(a-x-1):
        print(*z2[i])
    for i in range(a-x-1,a):
        for q,w in list(zip(z1[i-a+x+1],z2[i])):
            print(q+w,end=' ')
        print()
    for i in range(x+1,a):
        print(*z1[i])
