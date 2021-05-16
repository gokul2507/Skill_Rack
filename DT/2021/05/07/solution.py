x,y=map(int,input().split())
z=[]
t=''
for i in range(x):
    p=input().strip()
    t=p.replace("*","").replace(" ","")+t
    z.append(p.split())
t=list(t)
for i in z:
    for j in i:
        if j=="*":
            print(t.pop(0),end=' ')
        else:
            print(j,end=' ')
    print()