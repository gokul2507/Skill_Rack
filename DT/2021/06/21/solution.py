m=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
l=[]
for _ in range(int(input())):
    x,y,z=input().split("-")
    z,t=z.split(" ")
    x,z,t=int(x),int(z),int(t)
    l.append((z,y,x,t))
q=int(input())
l.sort(key=lambda i:(i[0],m.index(i[1]),i[2]))
w=1
for i in l:
    if i[-1]>=q:
        print("%02d-%s-%04d"%(i[2],i[1],i[0]))
        w=0
if w:
    print(-1)