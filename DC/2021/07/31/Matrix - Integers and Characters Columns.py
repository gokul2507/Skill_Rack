a,b=map(int,input().split())
z=[input().split() for i in range(a)]
z=list(zip(*z))
for i in z:
    s=0
    if i[0].isdigit():
        for j in i:
            s+=int(j) 
        print(s,end=' ') 
for i in z:
    if not i[0].isdigit():
        print(''.join(i[::-1]),end=' ')