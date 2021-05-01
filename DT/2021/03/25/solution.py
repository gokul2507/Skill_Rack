s,e=0,0
m=0
t=0
z=input().strip()
for i in range(1,len(z)):
    if int(z[i-1])%2==int(z[i])%2:
        if m<i-t:
            m=i-t
            s,e=t,i
        t=i
if i-t+1>m:
    print(z[t:i+1])
else:
    print(z[s:e])
