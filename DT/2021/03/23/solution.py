r,c,k=map(int,input().split())
l=[input().split() for _ in range(r)]
x,y,z=map(int,input().split())
ans=0
def check(q,m):
    #print(q,m,end='->')
    global ans
    w=0
    for j in q:
        if j=='0':
            w+=1
        else:
            if w>=k:
                ans+=w-k+1
            #print(w,end=' ')
            w=0
    if w>=k:
        ans+=w-k+1
for i in l:
    for j in [x,y,z]:
        q=i[:j]
        check(q,j)
        i=i[j:]
print(ans)
