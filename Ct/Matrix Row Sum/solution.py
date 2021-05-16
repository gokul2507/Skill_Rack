r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
for i in m:
    print(sum(i))