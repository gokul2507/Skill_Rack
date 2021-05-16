n,x=int(input()),1
for i in range((n//2)+1):
    t=(n-x)//2
    print('!'*t,'*'*x,'!'*t,sep='')
    x+=2
