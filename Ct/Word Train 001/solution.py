n=int(input())
l=[input().strip() for i in range(n)]
sl,el='',''
c=0
for i in l:
    sl+=i[0]
    el+=i[-1]
v=sl+el 
for i in sl:
    if v.count(i)==1:
        s=i 
while c<n:
    for i in l:
        if i[0]==s:
            s=i[-1]
            print(i) 
    c+=1 