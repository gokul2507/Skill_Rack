m={}
m['Jan']=31
m['Feb']=28
m['Mar']=31
m['Apr']=30
m['May']=31
m['Jun']=30
m['Jul']=31
m['Aug']=31
m['Sep']=30
m['Oct']=31
m['Nov']=30
m['Dec']=31
dd,mm,yy=input().split("-")
if dd.isalpha():
    mm,dd=dd,mm
dd=int(dd)
yy=int(yy)
if (yy%100 and yy%4==0) or yy%400==0:
    m['Feb']=29
l=list(m)
s=m[mm]-dd
t=s
for i in range(l.index(mm)+1,12):
    s+=m[l[i]]
print(s)
print(t)