input()
l=list(map(int,input().split()))
l1=[i%10 for i in l]
x,y=min(l1),max(l1)
a,b=[i for i in l if i%10==y],[i for i in l if i%10==x]
print(max(a)-min(b))