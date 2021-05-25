s=input().strip()
x=s[:len(s)//2]
y=s[len(s)//2:] 
if x<y:
    print(x,y,sep='\n') 
else:
     print(y,x,sep='\n')