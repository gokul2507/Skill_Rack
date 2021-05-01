a=int(input())
z=[[] for _ in range(a)]
t=1
for i in range(a):
    l=list(range(t,t+a-i))
    t+=a-i
    if i%2:
        l=l[::-1]
    for j in range(i,a):
        z[j].append(l.pop(0))
for i in z:
    print(*i)
