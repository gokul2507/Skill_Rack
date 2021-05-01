n=int(input())
if n==1: print(0);exit()
l=[0,1]
for i in range(n-2):
    l.append(int(str(l[-1])[::-1])+int(str(l[-2])[::-1]))
print(*l)
