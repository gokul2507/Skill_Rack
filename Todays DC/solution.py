s=int(input());a={}
for i in range(1,s+1):
    t=input().strip();a[t]=a.get(t,0)+1
    print(t,end="")
    if a[t]>1:
        print(a[t],end=" ")
    print()