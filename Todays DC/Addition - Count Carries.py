n=int(input())
m=int(input())
a,b=max(n,m),min(n,m)
l=len(str(a))-len(str(b))
a=list(map(int,str(a)))[::-1]
b=list(map(int,"0"*l+str(b)))[::-1]
f,c=0,0
for i,j in zip(a,b):
    if f+i+j>=10:
        f=1 
        c+=1
    else: f=0
print(c)