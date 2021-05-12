a=input().strip()
b=input().strip()[::-1]
for i in range(min(len(a),len(b))):
    if a[i]==b[i]:
        print(end=a[i])
