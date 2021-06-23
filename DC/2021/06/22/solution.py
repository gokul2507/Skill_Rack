x=input()
for i in range(1,int(x[1:-1])+1):
    t=i
    print(x[0]*i,end="")
    print(x[-1]*i,end="")
    while(t!=0):
        t-=1
        print(x[0]*t,end="")
        print(x[-1]*t,end="")
    print()