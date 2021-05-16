a=int(input())
t=[input().strip()]
z=[input().strip() for _ in range(a-1)]
l=len(t[0])
for i in z:
    while i:
        t.append(i[:min(len(i),l)]+("*"*(l-min(len(i),l))))
        i=i[min(len(i),l):]
for i in list(zip(*t)):
    print(*i)