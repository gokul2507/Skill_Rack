n=int(input())
l=sorted(list(map(int,input().split())))
l.append(-1)
c,x=0,0 
for i in range(n):
    if l[i+1]==l[i]+1:
        x=1 
    elif l[i+1]!=l[i]+1:
        c+=x 
        x=0
print(c)
