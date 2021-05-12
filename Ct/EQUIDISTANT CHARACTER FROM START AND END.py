a=input().strip()
l=(len(a)+1)//2
for i,j in zip(a[:l],a[::-1][:l]):
    if i==j:
        print(end=i)
