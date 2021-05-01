a=input().strip()
d={}
for i in a:
    d[i]=d.get(i,-1)+1
for i in d:
    if d[i]:
        print(i,end='')
