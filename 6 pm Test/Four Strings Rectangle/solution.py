z=[input().strip() for i in range(4)]
a,l=[z[0]],z[1:]
for i in range(1,4):
    for j in l:
        if j[0]==a[i-1][-1]:
            a.append(j)
            l.remove(j)
print(a[0])
x,y=len(a[0]),len(a[1]) 
ind=1 
for i in range(y-2):
    print(a[-1][-ind-1]+'*'*(x-2)+a[1][ind])
    ind+=1 
print(a[-2][::-1])