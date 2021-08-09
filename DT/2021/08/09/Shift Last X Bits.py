x,y=map(int,input().split())
x=bin(x)[2:]
l=len(x)
x="0"*(32-l)+x 
y,x=x[-y:],x[:-y]
y=y[-1:]+y[:-1]
print(int(x+y,2))