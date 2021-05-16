n=int(input())
z=[]
for i in range(n):
    a,b,c=input().split()
    b=int(b.replace(":",""))
    c=int(c.replace(":",""))
    z.append((a,b,c))
l=[]
x=int(input().strip().replace(":",""))
for i in z:
    if i[1]<=x<i[2]:
        l.append((i[1],i[0]))
l.sort()
for i in l:
    print(i[1])
if not l:
    print(-1)
