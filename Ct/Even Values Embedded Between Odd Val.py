a=int(input())
z=list(map(int,input().split()))[::-1]
l=[]
while z and z[0]%2==0:
    z.pop(0)
while z and z[-1]%2==0:
    z.pop()
if len(z)<3:
    print(-1)
else:
    for i in z:
        if i%2:
            continue
        print(i,end=' ')
