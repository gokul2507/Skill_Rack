z="abcdefghijklmnopqrstuvwxyz"
x=input().strip()
y=input().strip()
for i,j in zip(x,y):
    j=z.index(j)
    x=z.index(i)
    x=z[x:]+z[:x]
    print(end=x[j])
