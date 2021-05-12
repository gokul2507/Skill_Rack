s,v,c=input().strip(),'aeiouAEIOU',0
for i in range(len(s)-1):
    if s[i] in v and s[i+1] in v:
        c+=1 
print(c)
