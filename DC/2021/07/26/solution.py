n=int(input())
l=list(map(int,input().split()))
k=int(input())
x,s=k-1,0
for i in l:
    if(len(bin(i)[2:])>=k): s+=i ^ (1 << x)
    else:   s+=i 
print(s)