n=int(input())
s=[input().strip() for i in range(n)]
l=len(s[0])//4 
r,c=n*3,l*3 
m=[['*' for i in range(c)] for j in range(r)]
for i in range(n):
    m[i][l:l*2]=list(s[i][:l])
for i in range(n,n*2):
    m[i][:l]=list(s[i-n][-l:])
    m[i][-l:]=list(s[i-n][l:l*2])
for i in range(n*2,n*3):
    m[i][l:l*2]=list(s[i-n*2][l*2:l*3])
for i in m:
    print(*i,sep='')
