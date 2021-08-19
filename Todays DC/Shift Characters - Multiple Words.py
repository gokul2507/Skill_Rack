l=input().split()
z=[]
k,c=int(input()),0
for i in l:
    for j in range(k):
        i=i[-1]+i[:-1]
    z.append(i) 
for i in range(len(z)):
    if z[i]==l[i]:
        c+=1 
print(c)
print(*z)