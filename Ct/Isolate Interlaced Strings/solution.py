s=input().strip()
x=int(input())
a,b='',''
l1,l2=x,len(s)-x
i=0
while i<len(s):
    if len(a)<l1:
        a+=s[i]
        i+=1 
    if len(b)<l2:
        b+=s[i] 
        i+=1 
print(a,b,sep='\n')