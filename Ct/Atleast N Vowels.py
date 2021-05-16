a=input().strip()
c=int(input())
for i in a:
    if c:
        if i.lower() in "aeiou":
            c-=1
    else:
        break
if c:
    print("No")
else:
    print("Yes")
