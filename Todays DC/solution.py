r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
n=int(input())
for i in m:
    k=i[:n][::-1] 
    l=i[n:] 
    while k and l:
        print(k.pop(0) + l.pop(0),end=' ')
    print(*k,*l)