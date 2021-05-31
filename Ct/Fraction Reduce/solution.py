x,y=map(int,input().split('/'))
for i in range(2,16):
    if x%i==0 and y%i==0:
        x//=i 
        y//=i 
print(x,y,sep='/')