a,b=map(int,input().split())
m=[input().split() for i in range(a)]
x=input().strip()
for i in range(a-2):
    for j in range(b-2):
        if m[i+1][j+1]!=x[0]:
            continue
        l=m[i+1][j+2]
        l+="".join(m[i+2][j:j+3][::-1])+m[i+1][j]+"".join(m[i][j:j+3])
        for k in range(8):
            if m[i+1][j+1]+l==x:
                print("YES")
                exit()
            l=l[2:]+l[:2]
print("NO")
