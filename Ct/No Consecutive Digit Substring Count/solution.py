n=input().strip()
if not n:
    print()
    n=input().strip()
for _ in range(int(n)):
    x=input().strip()
    t=1
    p=x[0]
    s=0
    for i in x[1:]:
        if p==i:
            s+=(t*(t+1))//2
            t=1
        else:
            p=i
            t+=1
    print(s+(t*(t+1))//2)
