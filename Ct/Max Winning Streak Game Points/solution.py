input()
ma,s=0,0
for i in list(map(int,input().split())):
    if i<0:
        if s>ma:ma=s 
        s=0 
    else:
        s+=i
if s>ma:ma=s
print(ma)
