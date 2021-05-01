a,b=int(input()),int(input())
s=[]
for i in range(a,b+1):
    if int(i**0.5)==i**0.5:
        s.append(i)
print(*s,sep=',')
