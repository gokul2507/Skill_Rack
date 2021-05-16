input()
def ret():
    return list(map(int,input().split()))
a=ret()
b=ret()
c=ret()
d=ret()
q=0
for i in a:
    for j in b:
        for k in c:
            for l in d:
                if i+j==k+l or i+k==j+l or i+l==j+k:
                    q+=1
print(q)
