l=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
z=[]
for _ in range(int(input())):
    a,b,c=input().split("-")
    z.append((int(a),l.index(b),int(c)))
for i in sorted(z):
    print("%02d-%s-%04d"%(i[0],l[i[1]],i[2]))