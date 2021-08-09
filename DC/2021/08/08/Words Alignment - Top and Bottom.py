s=input().split()
l=0
for i in s:
    if len(i)>l:l=len(i)
for i in range(len(s)):
    if len(s[i])<l:
        s[i]=s[i]+"*"*(l-len(s[i])) if i%2==0 else "*"*(l-len(s[i]))+s[i]
z=[list(map(str,i)) for i in s]
for i in list(zip(*z)):
    print(*i)