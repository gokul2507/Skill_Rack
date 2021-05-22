l=list(map(int,input().split()))
f=0
while 1:
    try:
        l.append(int(input()))
        f=1 
    except:
        break 
if f: print(*l[::-1]) 
else:
    for i in l[::-1]:
        print(i)