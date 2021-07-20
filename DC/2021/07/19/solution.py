l=[]
while 1:
    try:
        s=input().split()
        l+=s
    except:
        break 
for i in l[::-1]:
    print(i[-1],end='')