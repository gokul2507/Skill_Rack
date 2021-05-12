a=int(input())
l=list(map(int,input().split()))
x=int(input())
z=[]
if a<=x:
    print(max(l))
    exit()
while len(l)>=x:
    z.append(l[:x])
    l=l[x:]
i=0
while l:
    z[i].append(l[0])
    l=l[1:]
    i+=1
    if i==len(z):
        i=0
for i in z:
    print(max(i),end=' ')
