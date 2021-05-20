s=[sorted(set(input().strip())) for i in range(int(input()))]
c,x=0,''
for i in s:
    x+=''.join(i)
for i in x:
    if x.count(i)==1:
        c+=1 
print(c)