r1,c1=map(int,input().split())
m1=[input().split() for _ in range(r1)]
r2,c2=map(int,input().split())
m2=[input().split() for _ in range(r2)]
r=int(input())
if r>r1 or r>r2:
    print(-1)
    exit()
def check(l):
    for i in range(r2-r+1):
        for j in range(c2-r+1):
            t=[]
            for q in range(i,i+r):
                for w in range(j,j+r):
                    t.append(m2[q][w])
            if t==l:
                for q in range(i,i+r):
                    for w in range(j,j+r):
                        print(m2[q][w],end=' ')
                    print()
                exit()
for i in range(r1-r+1):
    for j in range(c1-r+1):
        l=[]
        for q in range(i,i+r):
            for w in range(j,j+r):
                l.append(m1[q][w])
        check(l)
print(-1)
