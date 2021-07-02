cal=[input().split() for r in range(6)]
if len(cal[0])==6:
    cal.append(input().split())
    cal=[list(r) for r in zip(*cal)]
d=1
ds=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
h=False
for r in range(0,6):
    for c in range(0,7):
        if cal[r][c].isdigit():
            d+=1
        elif cal[r][c]=='#':
            print(d,ds[c])
            d+=1
            h=True
if h==False:
    print(-1)