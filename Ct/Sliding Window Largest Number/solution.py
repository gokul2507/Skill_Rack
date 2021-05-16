a,b,c=int(input()),int(input()),list(map(int,input().split()))
for i in range(len(c)-a+1):
    print(max(c[i:i+a]),end=' ')
