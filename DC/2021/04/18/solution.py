a=int(input())
d={}
for i,j in zip(input().split(),list(map(int,input().split()))):
    d[i]=d.get(i,[])+[j]
r,g,b=0,0,0
for i in range(1,1+int(input())):
    if 'R' in d:
        for j in range(len(d['R'])):
            if d['R'][j]:
                d['R'][j]-=1
                r+=1
    if i%2==0 and 'G' in d:
        for j in range(len(d['G'])):
            if d['G'][j]:
                d['G'][j]-=1
                g+=1
    if i%3==0 and 'B' in d:
        for j in range(len(d['B'])):
            if d['B'][j]:
                d['B'][j]-=1
                b+=1
print(r,g,b)
