a=int(input())
z=list(map(int,input().split()))
s=int(input())
z=sorted(z+[1+s])
print(sum(z[:z.index(s+1)]))