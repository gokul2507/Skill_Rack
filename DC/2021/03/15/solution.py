l=input().split(". ")
n1=int(input())
n=n1
if n<0:
    n*=-1 
    l=l[::-1] 
for i in l:
    if n-len(i.split())<=0:
        if (i==l[-1] and n1>0) or (i==l[0] and n1<0):
            print(i)
            exit()
        else:
            print(i,end='.')
            exit()
    else:
        n-=len(i.split())
