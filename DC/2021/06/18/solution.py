l=input().split()
f=1 
for i in range(len(l)):
    for j in range(len(l)):
        s=l[i]+l[j] 
        if s==s[::-1] and i!=j:
            print(s) 
            f=0 
if f:
    print(-1)