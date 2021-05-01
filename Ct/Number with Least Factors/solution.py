def fact(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    return c 
n=int(input())
l=sorted(list(map(int,input().split())))
mi,mim=fact(l[0]),l[0]
for i in l[1:]:
    if fact(i)<=mi:
        mi=fact(i)
        mim=i 
print(mim)
