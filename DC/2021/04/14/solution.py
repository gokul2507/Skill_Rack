s=input().strip()
x=0
for i in range(len(s)):
    for j in range(i,len(s)):
        c=int(s[i:j+1])
        if c%2:
            x=max(c,x)
print(x)
