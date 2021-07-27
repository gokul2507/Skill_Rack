l=[input().strip() for _ in range(int(input()))]
s=input().strip()
print(*sorted(l,key=lambda i:[s.index(j) for j in i]),sep='\n')