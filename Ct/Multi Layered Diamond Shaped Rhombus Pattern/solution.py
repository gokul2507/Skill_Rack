n=int(input())
l=[]
for i in range(n):
    s="#/"
    p=[n-i-1]+[1]*(i+1)
    q=""
    for j in p:
        q+=s[0]*j
        s=s[::-1]
    q+=q[::-1].replace('/','\\')
    print(q)
    l.append(q.replace('\\','-').replace('/','\\').replace('-','/'))
l=l[::-1]
print(*l,sep='\n')
