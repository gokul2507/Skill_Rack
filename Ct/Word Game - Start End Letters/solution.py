n=int(input())
l=[input().strip() for i in range(n)]
x,s=int(input()),input().strip()
l1=[s]
l.remove(s)
while l:
    for i in l:
        if l1[-1][-1]==i[0]:
            l1.append(i)
            l.remove(i)
            break 
    if len(l1)==x: 
        print(l1[-1])
        exit()
