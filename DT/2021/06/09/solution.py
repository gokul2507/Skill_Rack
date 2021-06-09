def getborder(z):
    t=z[0]
    x=z[-1][::-1]
    z=z[1:-1]
    z=list(zip(*z))
    return t+list(z[-1])+x+list(z[0][::-1])
r,c=map(int,input().split())
z1=getborder([input().split() for _ in range(r)])
z2=getborder([input().split() for _ in range(r)])
for i in range(r+r+c+c-4):
    if z1==z2:
        print("YES")
        exit()
    z1=z1[1:]+z1[:1]
print("NO")