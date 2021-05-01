s=input().strip()
c=0 
for i in range(1,len(s)):
    if len(set(s[:i]))==len(set(s[i:])):
        c+=1 
print(c)
