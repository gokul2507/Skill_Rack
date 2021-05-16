n=int(input())
z=input().split()
l=[]
while 1:
    q=''
    for i in range(3):
        t=z.pop(0)
        q+=t[-1]
        t=t[:-1]
        if t:
            z.append(t)
    l.append(int(q))
    if len(z)<3:
        print(sum(l))
        exit()
