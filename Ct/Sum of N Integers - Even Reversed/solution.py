n=int(input())
l=[i for i in list(map(int,input().split())) if i>0]
s=0 
for i in l:
    if i%2:s+=i 
    else:
        x=str(i)[::-1]
        s+=int(x)
print(s)
