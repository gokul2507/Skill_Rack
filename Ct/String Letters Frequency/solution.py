l={}
for i in input().strip():
    l[i]=l.get(i,0)+1 
for i in sorted(sorted(l),key=lambda i:l[i],reverse=True):
    print(i,l[i],sep='')