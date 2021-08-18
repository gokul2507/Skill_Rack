n=int(input())
a=sorted(map(int,input().split()))
x,y=-1,1
l=[]
for i in range(41):
    l.append(x+y)
    x,y=y,x+y
t=l.index(a[-1])
p=t
while a:
    if a.pop(-1)!=l[t]:
        print(l[t])
        exit()
    t-=1
print(l[p])