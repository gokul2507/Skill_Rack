s1,s2,s3=input().strip(),input().strip(),int(input())
day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
month={}
month['Jan']=31
month['Feb']=28
month['Mar']=31
month['Apr']=30
month['May']=31
month['Jun']=30
month['Jul']=31
month['Aug']=31
month['Sep']=30
month['Oct']=31
month['Nov']=30
month['Dec']=31
if (s3%100 and s3%4==0) or s3%400==0:
    month['Feb']+=1
s=day.index(s1)
for i in month:
    if i==s2:
        break
    for j in range(month[i]):
        s+=1
        s%=7
for i in range(month[s2]):
    if s==6:
        print("%02d-%s-%d"%(i+1,s2,s3))
    s+=1
    s%=7