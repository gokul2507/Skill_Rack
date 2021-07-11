r,c,s=0,0,0
while 1:
    try:
        l=list(map(int,input().split()))
        r+=1
        if c==0:
            c=len(l) 
        s+=sum(l)
    except:
        break 
print(r,c)
print(s)