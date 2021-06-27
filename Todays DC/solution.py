n=int(input())
m=[list(map(int,input().strip("*").split())) for i in range(n)] 
for i in range(n-2,-1,-1):
    for j in range(0,len(m[i])):
        m[i][j]+=max(m[i+1][j],m[i+1][j+1])
print(m[0][0])