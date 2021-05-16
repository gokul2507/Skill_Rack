a,b=map(int,input().split())
z=[list(map(int,input().split())) for _ in range(a)]
k,d=map(int,input().split())
for i in range(a-k+1):
    for j in range(b-k+1):
        for r in range(i,i+k):
            f=0
            for c in range(j,j+k):
                if int(str(z[r][c])[0])!=d:
                    f=1
                    break
            if f:
                break
        else:
            s=0
            for r in range(i,i+k):
                for c in range(j,j+k):
                    s+=z[r][c]
            print(s)
            exit()
print(-1)
