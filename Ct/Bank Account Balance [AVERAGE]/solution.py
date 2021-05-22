import math
p,n,l,x,y=map(int,input().split())
atmc,atm=1,0
for i in range(n):
    t=input().split()
    t[1]=int(t[1])
    if atmc>l:
        atm=1
    if t[0]=="CASH":
        p+=t[1]
    elif t[0]=="ATM":
        atmc+=1
        if atm:
            p-=x 
        p-=t[1] 
    elif t[0]=='CHQ':
        p+=t[1]
    elif t[0]=='CHQW':
        p-=t[1]
    elif t[0]=='INT':
        p+=t[1] 
    elif t[0]=='MNT':
        p-=t[1] 
    elif t[0]=="CARD":
        if t[1]>y:
            p+=math.floor(t[1]*0.1)
        p-=t[1] 
    else:
        p+=t[1] 
print(p)