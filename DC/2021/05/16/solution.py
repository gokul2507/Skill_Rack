get=lambda i,j:print(*[x*y for x,y in zip(i[int(j[0])-1],i[int(j[1])-1][::-1])])
get([list(map(int,input().split())) for _ in range(int(input().split()[0]))],input().split())