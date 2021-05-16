s=input().strip()
l=len(s)
t,f=1,0
x=1
for i in range(l):
    if s[i]!="*":
        c=s.count(s[i])
        s=s.replace(s[i],"*")
        for j in range(1,c+1):
            t*=j
for i in range(1,l+1):
    if i%10==0:
        f+=1
    else:
        x*=i
    if i==20:
        x*=2
print(x//t,end='')
print("0"*f)
