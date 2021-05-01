a=int(input())
a-=a%2
l=a//2+1
t=1
p=0
while p<l:
    p+=t
    t+=1
z=[]
p=0
for t in range(t-1,0,-1):
    q=[]
    for i in range(p,p+t*2,2):
        if i>a:
            i='X'
        q.append(i)
    p+=t*2
    z.append(q)
for i in z[::-1]:
    print(*i)
