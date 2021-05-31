n=int(input())
a=1;k=0;l=[];s=[];l1=[]
t=sum(range(1,n+1))
l=list(range(1,t+1))
for i in range(n):
    s=[]
    if (i%2==0):
        for j in range(n):
            if(i<=j):
                s.append(l[k])
                k+=1
            else:
                s.append(0)
        l1.append(s)
    else:
        for j in range(n-1,-1,-1):
            if(i<=j):
                s.append(l[k])
                k+=1
            else:
                s.append(0)
        l1.append(s[::-1])
for i in range(n):
    for j in range(n):
        if(j<=i):
            print(l1[j][i],end=' ')
    print()