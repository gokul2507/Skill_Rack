input()
for i in list(map(int,input().split())):
    if i%2:
        i*=i*i
    else:
        i*=i
    print(i,end=' ')
