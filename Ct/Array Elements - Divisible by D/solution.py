input()
z=list(map(int,input().split()))
d=int(input())
for i in z:
    if i%d==0:
        print(i,end=' ')
