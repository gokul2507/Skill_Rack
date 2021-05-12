l=""
a=int(input())
for j in range(a):
    t="* "*(a-j)
    for i in range(j):
        t+=str(i)+" "
    for i in range(j,-1,-1):
        t+=str(i)+" "
    t+="* "*(a-j)
    print(t)
    if j:
        t+="\n"
    l=t+l
print(*list(range(a)),*list(range(a,-1,-1)))
print(l)
