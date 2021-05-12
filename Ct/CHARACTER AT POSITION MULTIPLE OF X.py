a,b=map(str,input().split())
b=int(b)
i,j=1,0
while j!=len(a):
   if i%b==0:
       print(a[j],end='')
       if j==len(a)-1:break
   if j==len(a)-1:
    j=0
   else:j+=1
   i+=1
