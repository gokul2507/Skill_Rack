s=input().strip()
for i in range(len(s)):
    print(s[i::-1]+s[:-i-2:-1])