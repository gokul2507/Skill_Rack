a,b=[input().strip() for i in range(2)]
x,y=len(a)//2,len(b)//2 
s=''
for i in range(0,min(x,y)+1):
    s1=a[x-i:x+i+1]
    s2=b[y-i:y+i+1]
    if s1==s2:
        s=s1 
if not s:print(-1)
else:print(s)