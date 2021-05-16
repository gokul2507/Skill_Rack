n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    x=list(map(int,str(i)))
    s+=int(str(max(x))+str(i)+str(min(x)))
print(s)