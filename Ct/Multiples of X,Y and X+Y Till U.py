a,b=map(int,input().split())
c=a+b
l=[]
for i in range(1,int(input())):
    if 0 in [i%a,i%b,i%c]:
        l.append(i)
print(*l)
print(*l[::-1])
