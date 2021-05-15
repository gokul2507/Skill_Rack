e,o=[],[]
for i in input().strip():
    if i in "13579":
        o.append(i)
    else:
        e.append(i)
e.sort()
t=e[0]
e=e[1:]+o
e.sort(reverse=1)
print("".join(e)+t)