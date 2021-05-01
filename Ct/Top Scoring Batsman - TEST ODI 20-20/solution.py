l=[]
for i in range(int(input())):
    x=input().split()
    x[1]=int(x[1])
    x[2]=int(x[2])
    x[3]=int(x[3])
    x.insert(1,sum(x[1:]))
    l.append(x)
l=sorted(l,key=lambda i:i[-1],reverse=True)
l=sorted(l,key=lambda i:i[-2],reverse=True)
l=sorted(l,key=lambda i:i[-3],reverse=True)
l=sorted(l,key=lambda i:i[-4],reverse=True)
print(l[0][0])
