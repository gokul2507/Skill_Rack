a=int(input())
b=int(input())
z=[[1]*b]
for i in range(1,a):
    z.append([1]+[0]*(b-1))
for i in range(1,a):
    for j in range(1,b):
        z[i][j]=z[i][j-1]+z[i-1][j]
print(z[-1][-1])
