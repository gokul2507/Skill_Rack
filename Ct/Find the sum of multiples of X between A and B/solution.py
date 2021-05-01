a,b,c=[int(input()) for i in range(3)]
s=0
for i in range(b,c+1):
    if i%a==0:s+=i 
print(s)
