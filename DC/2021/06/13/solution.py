a,b=map(int,input().split())
for i in range(b):
    print(a,end=' ')
    a+=len(str(a))