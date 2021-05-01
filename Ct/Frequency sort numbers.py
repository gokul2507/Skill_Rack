a=int(input())
z=sorted(list(map(int,input().split())))
print(*sorted(z,key=z.count,reverse=1))
