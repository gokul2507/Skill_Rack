l=[input().strip() for i in range(4)]
l2=[l[0]]
l=l[1:]
for i in range(1,4):
    for j in l:
        if j[0]==l2[i-1][-1]:
            l2.append(j)
            l.remove(j)
print(l2[0])
a=len(l2[0])
b=len(l2[1])
ind=1
for i in range(b-2):
    print(l2[-1][-ind-1]+'*'*(a-2)+l2[1][ind])
    ind+=1
print(l2[-2][::-1])
