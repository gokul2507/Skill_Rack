a=int(input())
z=input().split()
x=input().strip()
if x not in z:
    print(-1,-1)
    exit()
print(z.index(x)+1,end=' ')
z=z[::-1]
print(a-z.index(x))
