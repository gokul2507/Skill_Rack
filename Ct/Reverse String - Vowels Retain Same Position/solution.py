a=input().strip()
b=[i for i in a if i not in 'aeiouAEIOU'][::-1]
for i in a:
    if i in 'aeiouAEIOU':
        print(i,end='')
    else:
        print(b.pop(0),end='')
