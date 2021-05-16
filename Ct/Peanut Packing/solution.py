n=int(input())
l=list(map(int,input().split()))
ma=l[0]
for i in range(1,n+1):
    if n%i==0:
        s=(n//i)*l[i-1]
        if ma<s:ma=s
    else:
        c=n%i
        s=l[i-1]*(n//i)+l[c-1] 
        if ma<s:ma=s
print(ma)
