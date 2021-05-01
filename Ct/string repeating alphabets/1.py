n=input().strip()
s=""
k=[]
for l in n:   
    if n.count(l)>1:  
        s+=l
for i in s:  
    if i not in k: 
        k.append(i)
for i in k:  
    print (i,end="")
