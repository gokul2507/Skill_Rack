n,c=int(input()),0
v=[int(i)for i in input().split()]
for i in range(1,n-1): 
    if v[i]>v[i-1] and v[i]>v[i+1]:
        c+=1;
print(c)
