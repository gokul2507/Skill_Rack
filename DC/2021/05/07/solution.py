n=int(input())
z=list(map(int,input().split()))
t=sorted(set(z))[::-1]
print(t.index(z[int(input())-1])+1)