h,m,s=0,0,0
z=[]
for _ in range(int(input())):
    x,y=map(int,input().split(":"))
    m+=x
    s+=y
    m+=s//60
    s%=60
    h+=m//60
    m%=60
    z.append("%02d:%02d:%02d"%(h,m,s))
print("Total Duration: %02d:%02d:%02d"%(h,m,s))
print(*z[:-1],sep='\n')