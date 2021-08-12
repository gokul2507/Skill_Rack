a=bin(int(input()))[2:]
s=input().strip()
t=''
for i,j in enumerate(a[::-1]):
    if j!='0':
        t+=chr(i+97).upper()
for i in s:
    if i not in t:
        print("NO")
        exit()
print("YES")