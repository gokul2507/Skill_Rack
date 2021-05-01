a=int(input())
z=list(input().split() for _ in range(a))
for i in list(zip(*z)):
    i=list(i)
    if i in z or i[::-1] in z:
        print("YES")
        exit()
print("NO")
