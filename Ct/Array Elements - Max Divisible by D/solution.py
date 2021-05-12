n=int(input())
l=list(map(int,input().split()))
x=int(input())
ma=-1
for i in l:
    if i%x==0 and ma<i:
        ma=i 
print(ma)
