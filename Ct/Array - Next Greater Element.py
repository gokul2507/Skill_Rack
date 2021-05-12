a=int(input())
l=list(map(int,input().split()))
for i in range(a):
    for j in range(i+1,a):
        if l[i]<l[j]:
            print(l[j],end=' ')
            break
    else:
        print(-1,end=' ')
