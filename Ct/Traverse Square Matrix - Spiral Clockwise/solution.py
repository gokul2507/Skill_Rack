z=[list(map(int,input().split())) for _ in range(int(input()))]
while z:
    print(*z[0],end=' ')
    z=list(zip(*z[1:]))[::-1]
