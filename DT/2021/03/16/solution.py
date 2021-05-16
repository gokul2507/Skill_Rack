n=int(input())
z=list(map(int,input().split()))
x,y=input().split()
x=int(x)
if y=='R':
    z=z[::-1]
t=z[0]-x
c=1
z=z[1:]
for i in z:
    if t<=0:
        break
    t=max(t,i)-x
    c+=1
print(c)
