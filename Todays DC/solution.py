a,b=map(int,input().split())
z=list(zip(*list(input().split() for _ in range(a))))
def getmax():
    ora,ap=0,0
    for i in z:
        if i[-1]=='O':
            ora+=1
        else:
            ap+=1
    if ora>ap:
        return 'O'
    return 'A'
for _ in range(int(input())):
    t=getmax()
    for i in range(b):
        z[i]=list(z[i])
        if z[i] and z[i][-1]==t:
            z[i]=['*']+z[i][:-1]
for i in list(zip(*z)):
    print(*i)