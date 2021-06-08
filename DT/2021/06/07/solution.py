a=int(input())
z=[-1 for _ in range(a+a+1)]
z[a]=1
def mod(x):
    c=0
    for i in x:
        if i==-1:
            print(end="- ")
        else:
            break
        c+=1
    print("".join(map(str,x)).replace("-1"," * ").strip(" * "))
for _ in range(a):
    mod(z[1:][:-1])
    l=[]
    for i in range(1,a+a):
        x=max(0,z[i-1])
        y=max(z[i+1],0)
        t=x+y
        if t==0:
            t=-1
        l.append(t)
    z=[-1]+l+[-1]