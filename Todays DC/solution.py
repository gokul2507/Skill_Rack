a,b =input().split();h1,m1=map(int,a.split(":"));h2,m2=map(int,b.split(":"));x,y=map(int,input().split());f=0
def add(h1,m1,x):  
    m1=m1+x  
    h=0    
    if(m1>=60):    
        h=m1//60   
        m1=m1%60  
    h1=h1+h  
    return(h1,m1)
def check(h1,m1): 
    h1,m1=add(h1,m1,x) 
    if(((h1*60)+m1)<=((h2*60)+m2)): 
        return 1   
    return 0
while(True): 
    if(check(h1,m1)):
        f=1     
        print("{}:{} -".format(str(h1).zfill(2),str(m1).zfill(2)),end=" ")    
        h1,m1=add(h1,m1,x)  
        print("{}:{}".format(str(h1).zfill(2),str(m1).zfill(2)))       
        h1,m1=add(h1,m1,y) 
    else:   
        break
if(f==0): 
    print(-1)