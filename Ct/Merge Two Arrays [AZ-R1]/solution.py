n=int(input())
l=[int(input()) for i in range(n)]
m=int(input())
l1=[int(input()) for i in range(m)]
print(*sorted(l+l1),sep='\n')
