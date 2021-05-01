from itertools import combinations 
s,n=map(int,input().split())
l,c=list(map(int,input().split())),0 
for i in range(1,len(l)):
    for j in combinations(l,i):
        if sum(j)==s:
            c+=1 
print(c)
