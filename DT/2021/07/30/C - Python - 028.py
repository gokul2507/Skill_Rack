l=[]
while 1:
    try:
        x=input().split()
        l.append(x) 
    except:
        break 
for i in l:
    for j in i:
        print(j,len(j),sep='',end=' ')
    print()