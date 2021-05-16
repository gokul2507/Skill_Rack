r,c=map(int,input().split())
mat=[input().split() for i in range(r)]
s,x=0,''
for i in mat:
    for j in i:
        if j.isdigit():s+=int(j) 
for i in zip(*mat):
    for j in i:
        if not j.isdigit():x+=j 
print(s,x,sep='\n')
