a=int(input())
z=list(map(int,input().split()))
for i in range(a-1,-1,-1):
    c=0
    for j in range(i-1,-1,-1):
        if z[i]<z[j]:
            c=z[j]
            break
    z[i]=c
print(*z)
