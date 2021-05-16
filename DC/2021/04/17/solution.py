a={}
for i in input().split():
    a[len(i)]=a.get(len(i),[])+[i]
f=1
for i in sorted(a):
    if i<=len(a[i]):
        f=0
        c=i
if f:
    print(-1)
else:
    for i in zip(map(list,a[c][:c])):
        print(*i[0])
