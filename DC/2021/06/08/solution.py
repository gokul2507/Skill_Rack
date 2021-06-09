a=input().strip()
v='aeiouAEIOU'
l=[i for i in a if i in v]
for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i] 
for i in a:
    if i in v:
        print(l.pop(0),end='')
    else:
        print(i,end='')