int(input())
a,s=list(map(int,input().split())),0
for i in a:
    if i>=10 and i<=99:
        s+=i
print(s)