n=int(input())
l=[]
l1=[input().strip().split() for i in range(n)]
l=[[i[1],i[0]] for i in l1]
l=sorted(l) 
for i in l:
    print(i[1],i[0],sep=' ')
