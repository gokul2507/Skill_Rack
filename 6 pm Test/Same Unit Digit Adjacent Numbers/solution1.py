c=0
a,b=map(int,input().split())
for _ in range(a):
    z=[i[-1] for i in input().split()]
    def check(p,x):
        try:
            if z[x-1]==p and x:
                return 1
            if z[x+1]==p:
                return 1
        except:
            try:
                return z[x+1]==p
            except:
                pass
        return 0
    for j in range(b):
        c+=check(z[j],j)
print(c)