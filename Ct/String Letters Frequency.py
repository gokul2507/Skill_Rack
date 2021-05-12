d={}
for i in input().strip():
    d[i]=d.get(i,0)+1
for i in sorted(sorted(d),key=lambda l:d[l],reverse=1):
    print(i,d[i],sep='')
