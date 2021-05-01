for i in range(1,int(input())+1):
    if i%2:print("*",*range(1,i+1),sep='')
    else:print(*range(1,i+1)[::-1],"*",sep='')
