a=int(input())
b=[1,2]
for i in range(2,a):
    b.append(i*b[i-2]+b[i-1])
print(b[a-1])
