n,k=map(int,input().split())
l,i=[n],0
while(l[i]%k==0):
    for j in range(k):
        l.append(l[i]//k)
    i+=1
print(*l)
