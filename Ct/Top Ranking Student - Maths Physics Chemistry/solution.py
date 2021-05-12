d={}
for i in range(int(input())):
    x=input().split()
    t=list(map(int,x[1:]))
    d[x[0]]=[sum(t)]+t
print(sorted(d.items(),key=lambda i:i[1])[-1][0])
