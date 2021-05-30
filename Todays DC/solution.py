def Sort(s):
    for i in s:
        if i.isalpha():
            return i
for i in sorted([input().split() for _ in range(int(input().split()[0]))][::-1],key=Sort):
    print(*i)