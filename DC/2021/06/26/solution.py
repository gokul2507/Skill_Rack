x=0
for i in range(1,int(input())+1):
    for j in range(i):
        print("- "*x,"* "*i,sep='')
    x+=i