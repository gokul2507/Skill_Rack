x,y=map(int,input().split())
for i in range(1,abs(x-y)+1):
    print(str(x)*i,*range(x+i,y+1),sep='')
for i in range(2,abs(x-y)+1):
    print(*range(x,y-i+1),str(y)*i,sep='')