z=[input().strip() for i in range(int(input()))]
c=0
for i in z:
    if len(set(i))>=c:
        s=''.join(i)
        c=len(set(i))
print(s)