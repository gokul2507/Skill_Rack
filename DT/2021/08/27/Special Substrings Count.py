s=input().strip()
c=0
for i in range(len(s)):
    for j in range(i,len(s)):
        x=s[i:j+1]
        l=len(x) 
        if l>2 and l%2:
            if len(set(x[:l//2]+x[l//2+1:]))==1:
                c+=1 
        elif len(set(x))==1:
            c+=1 
print(c)