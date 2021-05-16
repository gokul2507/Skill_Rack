a,b=[input().strip() for i in range(2)]
for i in range(len(a)):
    x=a[i:]
    if len(x)<=len(b):
        if a[i:]==b[:len(x)]:
            print(len(a)+len(b)-len(x))
            exit()
print(len(a)+len(b))
