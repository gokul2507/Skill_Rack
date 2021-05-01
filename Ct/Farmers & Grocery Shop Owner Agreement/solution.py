n=int(input())
l=list(map(int,input().split()))
l1=[]
p,c=l[n-1],0 
for i in range(n-1,-1,-1):
    if l[i]>=p:
        l1.append([p,c])
        p=l[i] 
        c=0 
    c+=1 
l1=l1[::-1] 
l1=sorted(l1,key=lambda i:i[1],reverse=True) 
print(l1[0][0])
