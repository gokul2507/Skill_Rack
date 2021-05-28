r,c=map(int,input().rstrip().split())
s1=input().rstrip()
s2=input().rstrip() 
mat=[]
for i in range(0,r*c,c): 
    if (i+c)>len(s1):  
        s1+=s1  
    else:    
        s1=s1   
    mat.append(s1[i:i+c]) 
count=0 
for i in mat: 
    for j in range(len(i)-len(s2)+1): 
        if s2==i[j:j+len(s2)]:  
            count+=1
for j in range(c):  
    l=[]     
    for i in mat:  
        l.append(i[j])  
    s=''.join(l)  
    for k in range(len(s)-len(s2)+1):  
        if s2==s[k:k+len(s2)]: 
            count+=1
print(count)