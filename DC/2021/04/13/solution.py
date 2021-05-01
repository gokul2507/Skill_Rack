a=int(input())
z=list(map(int,input().split()))
d=int(input())
while len(z)>=d:
    print(max(z[:d]),end=' ')
    z=z[d:]
