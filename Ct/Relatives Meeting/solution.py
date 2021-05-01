n=int(input())
l1,l=[],[]
for i in range(n):
    l1.append(list(map(int,input().split())))
for i in range(n):
    for y in l1:
        a,b=y[0],y[1]
        z=0
        for j in l:
            if a not in j and b not in j:
                z+=1 
                continue 
            elif b not in j:
                j.append(b)
            elif a not in j:
                j.append(a)
        if(z==len(l)):
            l.append([a,b])
x=int(input()) 
for j in l:
    if x in j:
        print(len(j))
        exit(0)
