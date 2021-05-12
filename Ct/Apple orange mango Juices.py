a,b=map(int,input().split())
c=1
for i in range(1,a+1):
    if i%b==0:
        c*=3
    else:
        c*=2
print(c)
