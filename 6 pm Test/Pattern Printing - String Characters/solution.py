s=input().strip()
for i in range(len(s)):
    for j in range(i+1):
        print(s[i],end='')
    print()