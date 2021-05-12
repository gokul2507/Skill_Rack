a=int(input())
z="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=""
while a>26:
    s+=z[(a%26)-1]
    a//=26
s+=z[a-1]
print(s[::-1])
