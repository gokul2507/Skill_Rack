a=int(input())
z=[]
for i in range(a):
    z.append(input().strip())
m=int(input())
l=len(z[0])
for i in range(a):
    for j in range(l):
        k=z[i][j]
        if 0<j<l-1:
            k=z[(i+m)%a][j]
        print(k,end="")
    print()
