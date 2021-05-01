a=int(input())
z=list(map(int,input().split()))
c=0
for i in range(1,a-1):
    if z[i-1]<z[i] and z[i]>z[i+1]:
        c+=1
print(c)
