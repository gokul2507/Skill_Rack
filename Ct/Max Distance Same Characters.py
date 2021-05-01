s,c=-1,0
l=""
a=input().strip()
for i in a:
    if a.count(i)>1 and i not in l:
        l+=i
        t=a.rfind(i)-a.find(i)
        if t>c:
            s=i
            c=t
if c:
    s+=str(c)
print(s)
