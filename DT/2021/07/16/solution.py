def pri(q,w):
    if q==' ':
        if w!=' ':
            q,w=w,'*'
        else:
            q,w='',''
    else:
        if w==' ':
            w='*'
    print(q+w)
a=input().strip()
b=input().strip()
while a and b:
    x,y=a[0],b[0]
    a,b=a[1:],b[1:]
    pri(x,y)
if not a:
    a=b
for i in a:
    if i==' ':
        i='*'
    print(i+"*")