x,y=map(int,input().split())
c=0
x=bin(x)[2:]
for i in input().split():
    if x.endswith(bin(int(i))[2:]):
        c+=1
print(c)