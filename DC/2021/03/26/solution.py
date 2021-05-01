a,b=input().strip(),input().strip()
v='aeiouAEIOU'
x,y=[i for i in a if i in v],[i for i in b if i in v]
for i in a:
    if i in v:print(y.pop(0),end='')
    else:print(i,end='')
print()
for i in b:
    if i in v:print(x.pop(0),end='')
    else:print(i,end='')
