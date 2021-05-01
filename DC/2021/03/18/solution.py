r,c=map(int,input().split()) 
m=[list(map(int,input().split())) for i in range(r)]
x=int(input())
d,f=-1,0 
while 1:
    if f<x or 0 not in m[r-f-1]:
        if d==-1:
            print("L",c)
        else:
            print("R",c)
        print("U")
        f+=1 
        d*=-1
    else:
        if d==1:
            print("R",m[r-f-1].index(0)+1)
        else:
            print("L",m[r-f-1][::-1].index(0)+1)
        break
