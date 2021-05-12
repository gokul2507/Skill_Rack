n=int(input())
l=sorted(list(map(int,input().split())))
l1=sorted(list(map(int,input().split())))
s=0 
for i in range(n):
    s+=abs(l[i]-l1[i])
print(s)
