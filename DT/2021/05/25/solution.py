a=input()
a=sorted(list(a.strip()))+['1']
c=0
f=0
for i in range(len(a)-1):
    if ord(a[i])+1!=ord(a[i+1]):
        if f>=1:
            c+=1
        f=0
    else:
        f+=1
if c==0:
    c=-1
print(c)