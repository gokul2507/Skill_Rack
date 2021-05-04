s=input().strip()
a,b=map(str,input().split())
if a==b and s.count(b)==1:
    print(len(s)-1)
    exit()
c1,c2=[],[]
for i in range(len(s)):
    if s[i]==b:
        c1.append(i)
    if s[i]==a:
        c2.append(i)
t=len(s)
for i in c1:
    for j in c2:
        if i!=j:
            t=min(abs(i-j),t)
print(max(t-1,0))