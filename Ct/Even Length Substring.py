def fsum(a):
    l=len(a)
    a=list(map(int,list(a)))
    if sum(a[:l//2])==sum(a[l//2:]):
        return 1
    return 0
a=input().strip()
l=""
for i in range(len(a)):
    for j in range(i+2,len(a)+1,2):
        if fsum(a[i:j]) and j-i>len(l):
            l=a[i:j]
if not l:
    l=-1
print(l)
