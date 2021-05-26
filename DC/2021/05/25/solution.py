x,y=map(int,input().split())
x=bin(x)[2:]
c=0
for i in range(1,len(x)+1):
    if int(x[:i],2)%y==0:
        c+=1
print(c)