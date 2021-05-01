a='abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    x=input().strip()
    y=x.lower().index(a[i%26])
    print(x[y:])
