l=input().strip()+"V"
f=0
s=''
for i in l:
    if i.isdigit():
        s+=i 
    else:
        if len(s)==3:
            print(s,end=' ')
            f=1 
        s='' 
if f==0:
    print(-1)
