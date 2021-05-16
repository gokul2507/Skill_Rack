input()
l=list(map(int,input().split()))
print(len([i for i in set(l) if l.count(i)>1]))
