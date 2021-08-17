s1,s2,s3=[input().strip() for i in range(3)]
l=max([len(s2),len(s3)])
m=[["*" for i in range(len(s1))]for j in range(l)]
m[0]=list(s1)
f,f1=1,1
for i in range(len(s1)):
    if m[0][i]==s2[0] and f:
        for j in range(1,len(s2)):
            m[j][i]=s2[j]
            f=0
    elif m[0][i]==s3[0] and f1:
        for j in range(1,len(s3)):
            m[j][i]=s3[j]
            f1=0
for i in m:
    print(*i,sep='')