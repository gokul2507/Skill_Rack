r,c=map(int,input().split())
m=[input().split() for i in range(r)]
z,count=[['0']*c for i in range(r)],0
for i in range(r):
    for j in range(c):
        if m[i][j]=='S':
            for i1 in range(max(0,i-1),min(r,i+2)):
                for j1 in range(max(0,j-1),min(c,j+2)):
                    z[i1][j1]='*' 
        elif m[i][j]=='L':
            for i1 in range(max(0,i-2), min(r,i+3)):
                for j1 in range(max(0,j-2),min(c,j+3)):
                    z[i1][j1]='*' 
for i in z:
    count+=i.count('*') 
print(count)