n=int(input())
a,b,c='','',''
for i in range(n):
    s=input().strip()
    a+=s[:i+1]
    b+=s[i+1:len(s)-(i+1)]
    c+=s[len(s)-(i+1):] 
print(a,b,c,sep='\n')