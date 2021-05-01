l=list(map(int,input().split()))
for i in range(len(l)-1):
    if l[i]>max(l[i+1:]):
        print(l[i],end=' ')
print(l[-1])
