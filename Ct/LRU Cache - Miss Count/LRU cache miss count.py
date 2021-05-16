s,n=map(int,input().strip().split(" "))
p=list(map(int,input().strip().split(" ")))
c,m=[],0
for i in p:   
    if i in c: 
        c.remove(i)  
    else:   
        if len(c)>=s: 
            c.pop(0)   
        m+=1  
    c.append(i)
print(m)
