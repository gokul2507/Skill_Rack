r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
k=int(input())
for i in range(k):
    for j in range(r//2):
        m[j][:c//2],m[j][c//2:],m[r//2+j][c//2:],m[r//2+j][:c//2]=m[r//2+j][:c//2],m[j][:c//2],m[j][c//2:],m[r//2+j][c//2:]
for i in m:
    print(*i)