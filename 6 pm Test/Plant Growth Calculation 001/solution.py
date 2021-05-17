def prime(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0 
    return 1 
def find(n):
    while not prime(n):
        if n<2:
            return 0
        n-=1
    return n
r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
x=int(input())
for t in range(x):    
    for i in range(r):
        for j in range(c):
            temp=m[i][j]
            if prime(m[i][j]):
                p=m[i][j]-1 
                m[i][j]+=m[i][j]-find(p)
            else:
                if j<c-1:
                    m[i][j]+=m[i][j+1]%10
                if j:
                    m[i][j]+=prev%10
            prev=temp
for i in m:
    print(*i)