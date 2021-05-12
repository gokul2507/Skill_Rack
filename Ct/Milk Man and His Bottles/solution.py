dp=[float("inf")]*(10001)
dp[0]=0
for i in range(1,10001):
    for j in [1,5,7,10]:
        if j<=i and dp[i-j]!=float("inf"):
            dp[i]=min(dp[i],dp[i-j]+1)
for _ in range(int(input())):
    print(dp[int(input())])
