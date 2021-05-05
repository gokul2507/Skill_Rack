a=int(input())
l=[]
m=100
for _ in range(a):
    l.append(input().strip())
    m=min(m,len(l[-1]))
while l:
    i=0
    t=100
    while i<len(l):
        print(l[i][:min(len(l[i]),m)])
        l[i]=l[i][min(len(l[i]),m):]
        if l[i]:
            t=min(t,len(l[i]))
            i+=1
        else:
            l.pop(i)
    m=t