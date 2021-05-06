a,b=map(int,input().split())
z=[input().split() for _ in range(a)]
k=int(input())
for i in range(a-k+1):
    for j in range(b-k+1):
        if z[i][j]==z[i+k-1][j] and z[i+k-1][j]==z[i+k-1][j+k-1] and z[i][j]==z[i][j+k-1]:
            for r in range(i,i+k):
                z[r][j+r-i]="*"
                z[r][j+k-1-r+i]="*"
            for r in z:
                print(*r)
            exit()