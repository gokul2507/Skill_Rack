y,m={},{}
l=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in range(int(input())):
    x=input().strip().split('-')
    y[x[2]]=y.get(x[2],0)+1 
    m[x[1]]=m.get(x[1],0)+1
y=sorted(y.items(),key=lambda i:i[0])
m=sorted(m.items(),key=lambda i:l.index(i[0]))
y=sorted(y,key=lambda i:i[1],reverse=1) 
m=sorted(m,key=lambda i:i[1],reverse=1) 
my,mm=y[0][1],m[0][1] 
for i in y:
    #print(i)
    if i[1]==my:
        print(i[0],end=' ')
print()
for i in m:
    if i[1]==mm:
        print(i[0],end=' ')