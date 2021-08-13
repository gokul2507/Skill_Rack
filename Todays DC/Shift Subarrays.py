int(input())
l=list(map(int,input().split()))
for i in range(int(input())):
    a,b,s=map(str,input().split())
    a,b=int(a)-1,int(b)-1 
    if s=='L':
        l=l[:a]+l[a+1:b+1]+[l[a]]+l[b+1:]
    else:
        l=l[:a]+[l[b]]+l[a:b]+l[b+1:]
    print(*l)