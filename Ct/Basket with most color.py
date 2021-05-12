a=int(input())
l=list(map(str,input().strip().split()))
z=[]
z.append(str(set(l[0]+l[1]))) 
for i in range(1,a-1):
    z.append(str(set(l[i-1]+l[i+1]+l[i]))) 
z.append(str(set(l[-1]+l[-2])))
max=len(z[0])
m=1
for i in z:
    if len(i)>max:
        max=len(i)
        m=z.index(i)+1 
print(m)
