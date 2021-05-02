
x,y=map(int,input().split())
z=[input().strip().split() for _ in range(x)]
t="-1"
s=input().strip()
def check(p):
    return s in p or s in p[::-1]
if check("".join(z[0])):
    t="Top"
elif check("".join(list(zip(*z))[-1])):
    t="Right"
elif check("".join(z[-1])):
    t="Bottom"
elif check("".join(list(zip(*z))[0])):
    t="Left"
print(t)