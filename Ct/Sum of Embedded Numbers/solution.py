n=input().strip()+' '
c=0
x=''
for i in n:
    if i.isdigit():
        x+=i 
    else:
        if len(x):c+=int(x)
        x=''
print(c)
