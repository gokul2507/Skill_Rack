n=int(input())
z=[input().split() for _ in range(n)]
a=input().strip()
b=input().strip()
def check(f,o):
    f="".join(f)
    return f==o or f==o[::-1]
def qwe(p):
    t1,t2=False,False
    for i in range(n):
        for j in range(n-len(a)+1):
            if check(p[i][j:j+len(a)],a) and not t1:
                t1=True
                break
            if check(p[i][j:j+len(b)],b):
                t2=True
                break
    if t1 and t2:
        print("YES")
        exit()
qwe(z)
qwe(list(zip(*z)))
print("NO")