s=input().strip()
l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    if s.count(i)>1:
        print(i,end='')