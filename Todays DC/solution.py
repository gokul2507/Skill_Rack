n=int(input())
m=[list(map(str,input().split())) for i in range(n)]
a1,b1,a2,b2,a3,b3,a4,b4=0,0,0,n-1,n-1,0,n-1,n-1
for i in range(n//2):
    a,b,c,d=m[a1][b1],m[a2][b2],m[a3][b3],m[a4][b4]
    m[a1][b1]=b
    m[a2][b2]=d
    m[a3][b3]=a 
    m[a4][b4]=c 
    a1,b1,a2,b2,a3,b3,a4,b4=a1+1,b1+1,a2+1,b2-1,a3-1,b3+1,a4-1,b4-1
for i in m:
    print(*i)