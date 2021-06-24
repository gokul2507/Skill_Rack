import datetime
x,y=int(input()),int(input())
t=datetime.datetime(y,1,1)
p=1
while 1:
    t+=datetime.timedelta(x,0)-datetime.timedelta(p,0)
    p=0
    if int(t.strftime("%Y"))<=y:
        print("%s-%s-%04d"%(t.strftime("%d"),t.strftime("%b"),int(t.strftime("%Y"))))
    else:
        break