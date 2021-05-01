ans=0
def check(l,s,m):
    global ans
    if s>m:
        return 
    if s==m:
        ans+=1
        return
    for i in range(len(l)):
        check(l[i+1:],s+l[i],m)
a=int(input())
check(list(map(int,input().split())),0,int(input()))
print(ans)
