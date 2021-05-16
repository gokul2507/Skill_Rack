a,o='.','.'
x,y=map(int,input().split())
for i in range(x,y+1):
    if i%2:
        if a=='.':
            a=i
        else:
            a&=i
    else:
        if o=='.':
            o=i
        else:
            o|=i
print(a^o
