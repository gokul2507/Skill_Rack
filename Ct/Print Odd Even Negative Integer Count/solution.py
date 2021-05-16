n=int(input())
l=list(map(int,input().split()))
e,o,n=0,0,0
for i in l:
    if i%2 and i>0:o+=1 
    elif i==0:e+=1
    elif i%2==0 and i>0:e+=1 
    else:n+=1 
print(o,e,n)
