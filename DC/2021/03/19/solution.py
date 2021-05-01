import re
x,y=map(int,input().split())
l=0
for i in range(5,x+1):
    if len(re.findall('(?=101)',bin(i)[2:]))>=y:
        l+=1
print(l)
