r,c=list(map(int,input().split())),list(map(int,input().split()))
a=int(input())
if r[1]==c[1]:
    l=abs(r[0]-c[0]) 
    b=a//l 
    print(r[0],(r[1]+b))
    print(c[0],(c[1]+b))
else:
    b=abs(r[1]-c[1])
    l=a//b 
    print((r[0]+l),r[1])
    print((c[0]+l),c[1])
