l=[sorted(set(input().strip())) for i in range(int(input()))]
s,c='',0
for i in l:
    s+=''.join(i)
for i in set(s):
    if s.count(i)==len(l):
        c+=1 
print(c)