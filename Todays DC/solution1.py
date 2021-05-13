d={}
for i in input().split("-"):
    s,n='',''
    for j in i:
        if j.isdigit():
            n+=j
        else:
            s+=j
    d[int(n)]=s
for i in sorted(d):
    print(end=d[i])