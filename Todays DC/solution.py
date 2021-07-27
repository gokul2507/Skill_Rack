import datetime 
s=input().strip()
k,x=map(int,input().split())
a=datetime.datetime.strptime(s,"%I:%M:%S")
b=datetime.datetime.strptime(s,"%I:%M:%S")
f=60*60*12
for i in range(x%f):
    a+=datetime.timedelta(seconds=1) 
for i in range((x//k)%f):
    b+=datetime.timedelta(seconds=1) 
print(a.strftime("%02I:%02M:%02S"),b.strftime("%02I:%02M:%02S"),sep='\n')