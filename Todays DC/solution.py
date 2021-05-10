def getnum(n):
    for i in range(0,5):
        for j in range(0,5):
            if s[i][j]==n:
                if j==2:
                    if i==0:
                        return 12
                    else:
                        return 6 
                elif j>2:
                    return i+1
                else:
                    return 12-i-1
s=[list(map(str,input().split())) for i in range(5)]
h,m=map(str,input().split())
hr=getnum(h)
mi=getnum(m)*5 
if mi==60:
    mi=0 
print("%02d:%02d"%(hr,mi))