p='()'
s=''
x,y=map(int,input().split())
for i in range(x):
    s,p=s+p,s
    if i>1:
        s='('+s+')'
print(s[y-1])