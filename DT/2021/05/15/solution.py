a,b=map(int,input().split())
z=list(zip(*list(input().split() for _ in range(a))))
s=0
for i in z:
    i="".join(i)
    s+=max(int(i,2),int(i[::-1],2))
print(s)