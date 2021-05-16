a,b,c,s=[input().strip() for i in range(4)]
x,l=0,2
for i in s:
    if i in a:
        x+=abs(l-3)
        l=3
    elif i in b:
        x+=abs(l-2)
        l=2
    else:
        x+=abs(l-1)
        l=1
print(x)
