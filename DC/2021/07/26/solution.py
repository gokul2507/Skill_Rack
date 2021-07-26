from datetime import datetime,timedelta
strf=lambda i,j:i.strftime(j)
qwe=lambda i:"%s-%s-%04d"%(strf(i,"%d"),strf(i,"%b"),int(strf(i,"%Y")))
display=lambda i:print(*i,sep='\n') 
days=list(map(int,input().split()))
year=int(input())
date=datetime(year,1,1)
city=[[],[]]
change=False
while 1:
    sd=date
    ed=date+timedelta(days=days[0]-1)
    if int(sd.strftime("%Y"))!=year:
        break
    if int(ed.strftime("%Y"))!=year:
        city[0].append("%s to %s-%04d"%(qwe(sd),"31-Dec",year))
        break
    city[0].append("%s to %s"%(qwe(sd),qwe(ed)))
    date+=timedelta(days=days[0])
    city=city[::-1]
    days=days[::-1]
    change=not change
if change:
    city=city[::-1]
print("City A:")
display(city[0])
print("City B:")
display(city[1])