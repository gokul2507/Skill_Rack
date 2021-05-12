a,b,c="","",""
for i in range(1,int(input())+1):
    s=input().strip()
    a+=s[:i]
    b+=s[i:-i]
    c+=s[-i:]
print(a,"\n",b,"\n",c)
