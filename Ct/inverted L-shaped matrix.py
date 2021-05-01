a=int(input())
z=list(list(map(int,input().split())) for _ in range(a))
q=[]
while z:
    t=z.pop()
    for i in range(len(z)-1,-1,-1):
        if z[i]:
            t.append(z[i].pop())
    q.append(t)
for i in q[::-1]:
    print(*i)
