x=int(input())
for i in list(zip(range(1,x+1),range(x,0,-1))):
    print(*i,end=' ')
