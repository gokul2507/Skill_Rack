s=input().strip()
z=True if s[0]=='T' else False 
for i in range(1,len(s)):
    if not s[i].isalpha():
        if s[i]=='&':
            z&=True if s[i+1]=='T' else False 
        elif s[i]=='|':
            z|=True if s[i+1]=='T' else False 
        elif s[i]=='^':
            z^=True if s[i+1]=='T' else False 
print("T") if z else print("F")