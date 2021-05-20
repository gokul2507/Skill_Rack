n,m,a=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
c=0
for i in s[:a-1]:
    for j in range(n):
        if l[j]%i==0 and l[j]>0:
            l[j]=0
for i in l:
    if i and i%s[a-1]==0:
        c+=1 
print(c)