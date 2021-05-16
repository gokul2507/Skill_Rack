a=input()
l=input().split()
c=0
for i in set(l):
    c+=l.count(i)//2
print(c)
