n=int(input())
a,d='a',1
def get(s):
    global a
    if s=='a':
        l=[]
        for i in range(n):
            l.append(a)
            if a=='z':
                a='a'
            else:
                a=chr(ord(a)+1)
        return l
    return [d+i for i in range(n)]
q="a0"
if n%2:
    q="0a"
for i in range(n):
    if q[0]=='a':
        print(*get("a"))
    else:
        print(*get("0"))
        get("a")
    d+=n
    q=q[::-1]