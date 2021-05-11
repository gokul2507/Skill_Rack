a=int(input())
z=list(map(int,input().split()))
t=max(z)
for i in range(t):
    for j in z:
        s="* "*j
        if i+1<=j:
            s=(str(j)+" ")*j
        print(s,end='')
    print()