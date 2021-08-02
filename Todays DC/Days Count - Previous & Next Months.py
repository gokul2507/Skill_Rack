import datetime 
from calendar import monthrange
s=input().strip()
d=datetime.datetime.strptime(s,"%d-%b-%Y").replace(day=1)
l=d - datetime.timedelta(days=1) 
n=d + datetime.timedelta(days=31) 
print(l.strftime("%B %Y -"),monthrange(l.year,l.month)[1],"days")
print(n.strftime("%B %Y -"),monthrange(n.year,n.month)[1],"days")