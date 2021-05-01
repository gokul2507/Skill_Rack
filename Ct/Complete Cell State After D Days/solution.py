def cellCompete(l,n):
    t=0
    for i in range(n):
        for j in range(0,8):
            if j==0:
                p=0 
            else:
                p=t 
            if j==7:
                n=0 
            else:
                n=l[j+1] 
            t=l[j] 
            if p==n:
                l[j]=0 
            else:
                l[j]=1 
    return l
