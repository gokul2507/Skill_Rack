def calc(a):
    t=""
    d=""
    for i in a+"+":
        if i.isdigit():
            t+=i
        else:
            if not d:
                r=t
            else:
                r=str(int(eval(r+d+t)))
            d=i
            t=""
    return r
l,r=[],[]
for i in range(int(input())):
    t=input().strip()
    t=t[t.index('.')+1:].split()
    l.append(calc(t[0]))
    r.append(t[1])
for i in l:
    print(r.index(i)+1,end=' ')
