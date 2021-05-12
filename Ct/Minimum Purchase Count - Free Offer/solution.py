n,l=int(input()),sorted(list(map(int,input().split())))
l1,c=l[0],1 
for i in l:
    if i<=l1+4:continue 
    else:c+=1;l1=i 
print(c)
