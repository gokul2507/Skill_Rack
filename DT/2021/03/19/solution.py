r1,c1=map(int,input().split())
m1=[input().split() for _ in range(r1)]
r2,c2=map(int,input().split())
m2=[input().split() for _ in range(r2)]
x=int(input())
for i in range(r1-x+1):
    for j in range(c1-x+1):
        m1l=[]
        for m1r in range(i,i+x):
            for m1c in range(j,j+x):
                m1l.append(m1[m1r][m1c])
        for I in range(r2-x+1):
            for J in range(c2-x+1):
                m2l=[]
                for m2r in range(I,I+x):
                    for m2c in range(J,J+x):
                        m2l.append(m2[m2r][m2c])
                if m2l==m1l:
                    for m2r in range(I,I+x):
                        for m2c in range(J,J+x):
                            print(m2[m2r][m2c],end=' ')
                        print()
                    exit()
print(-1)
