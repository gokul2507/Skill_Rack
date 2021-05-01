r,c=map(int,input().split())
l=[input().split() for i in range(r)]
for i in l:
    for j in range(0,len(l[0][0]),3):
        for a in i:
            print(*a[j:j+3],end=' ')
        print()
