a,b=input().split()
for i in range(len(a)):
    if a==b:
        print("Yes")
        exit()
    a=a[1:]+a[:1]
print("No")
