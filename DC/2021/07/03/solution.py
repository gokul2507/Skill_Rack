def getRow(ch):
    for i in range(3):
        if ch in keys[i]:return i 
keys=[input().strip() for _ in range(3)]
s=input().strip()
indexs,ind,count,prevMaxCount=[],getRow(s[0]),1,1
for i in range(1,len(s)):
    if getRow(s[i])==getRow(s[i-1]):
        ind,count=getRow(s[i]),count+1 
    else:
        if count>prevMaxCount:
            indexs=[ind]
            prevMaxCount=count
        elif prevMaxCount==count and count>1:
            indexs.append(ind)
            prevMaxCount=count
        count,ind=1,getRow(s[i])
if len(s)>1 and getRow(s[-1])==getRow(s[-2]):
    if count>prevMaxCount:
        indexs=[ind]
    elif count==prevMaxCount and count>1:
        indexs.append(ind)
if indexs:
    indexs=sorted(set(indexs))
    for ind in indexs:
        print(keys[ind])
else:
    print(-1)