n,k=map(int,input().split())
l=list(map(int,input().split()))
c,l1=0,[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==k and l[i] not in l1:c+=1;l1.append(l[i]);break
        if l[i]+l[j]==k and [l[i],l[j]] not in l1 and [l[j],l[i]] not in l1:
            c+=1
            l1.append([l[i],l[j]]);l1.append([l[j],l[i]])
print(c)
