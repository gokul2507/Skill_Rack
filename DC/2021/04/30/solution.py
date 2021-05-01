d={}
l=[]
a=int(input())
for i in range(a):
    x,y=input().strip().split(" - ")
    d[x]=y
    l.append(x)
for i in range(a):
    for j in range(i+1,a):
        print("%s vs %s (%s)"%(l[i],l[j],d[l[i]]))
        print("%s vs %s (%s)"%(l[j],l[i],d[l[j]]))
