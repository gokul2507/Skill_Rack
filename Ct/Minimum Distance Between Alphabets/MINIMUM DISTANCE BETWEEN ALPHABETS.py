a=input().strip()
x,y=input().strip().split()
q,w=[],[]
for j,i in enumerate(a):
    if i==x:
        q.append(j)
    if i==y:
        w.append(j)
c=len(a)
for i in q:
    for j in w:
        if i!=j:
            c=min(c,abs(i-j)-1)
print(c)
