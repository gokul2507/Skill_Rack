def findCount(a,si,ei): 
    rc=0   
    if ei-si==0: 
        rc+=1   
        return rc  
    m=999999   
    for i in range(si,ei+1):     
        if a[i]<m:     
            m=a[i]  
    rc+=m   
    for i in range(si,ei+1):
        a[i]-=m  
    sti,eti=-1,-1  
    for i in range(si,ei+1):  
        if a[i]>0 and sti==-1:    
            sti=i      
        if a[i]==0 and sti!=-1 and eti==-1:   
            eti=i-1          
            rc+=findCount(a,sti,eti)     
            sti,eti=-1,-1  
    if sti!=-1 and eti==-1:    
        eti=ei     
        rc+=findCount(a,sti,eti)  
    return min(rc,ei-si+1)
n=int(input())
a=list(map(int,input().strip().split()))
print (min(n,findCount(a,0,n-1)))
