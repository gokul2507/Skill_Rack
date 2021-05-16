def get(p):
    a,n='',''
    for i in p:
        if i.isalpha():
            a+=i
        else:
            n+=i
    return a,int(n)
r,c=map(int,input().split())
z=[]
for _ in range(r):
    t=[]
    for i in input().split():
        x,y=get(i)
        t.append((x,y,i))
    z.append(t)
z=list(zip(*z))
for i in range(c):
    z[i]=sorted(z[i])
z=list(zip(*z))
for i in z:
    t=0
    for j in i:
        t+=j[1]
    print(t)
