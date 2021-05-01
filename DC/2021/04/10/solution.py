def find(x):
    for i in range(5):
        for j in range(5):
            if x==m[i][j] or x in m[i][j]:
                return [i+1,j+1]
m=[input().split() for i in range(5)]
s=input().strip()
for i in s:
    if i.isalpha():print(*find(i),sep='',end='')
    else:print(end=" ")
