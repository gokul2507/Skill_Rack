def fun(x):
    l=len(x)//4
    return [x[:l],x[l:l+l],x[l+l:l+l+l],x[l+l+l:]]
for _ in range(int(input())//2):
    for i,j in zip(fun(input().strip()),fun(input().strip())):
        print(i+j)