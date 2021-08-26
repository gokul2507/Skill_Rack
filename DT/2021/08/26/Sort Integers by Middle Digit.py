def func(x):
    l=len(x)
    return int(x[l//2])
n=int(input())
l=sorted(map(int,input().split()))
l=sorted(l,key=lambda i:func(str(i)))
print(*l)