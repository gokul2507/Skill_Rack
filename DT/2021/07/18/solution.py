def is_valid(d,m,y):   
    if m=='Feb':    
        if d==29:  
            if ((y%400==0) or (y%100 and y%4==0)):  
                return 1    
            return 0   
        if d>29:    
            return 0   
        return 1 
    q=['Jan','Mar','May','Jul','Aug','Oct','Dec']  
    if m not in q and d!=31:
        return 1 
    if m in q:  
        return 1 
    return 0
input()
d=list(map(int,input().split()))
input()
m=input().split()
input()
y=list(map(int,input().split()))
mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in sorted(y)[::-1]: 
    for j in sorted(m,key=lambda w:-mon.index(w)-1):
        for k in sorted(d)[::-1]: 
            if is_valid(k,j,i):  
                print("%02d-%s-%04d"%(k,j,i))
                exit()