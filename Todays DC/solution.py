N=int(input());numList = input().split();s=0
for num in numList:   
    s+=int(str(len(num))+num)
print(s)