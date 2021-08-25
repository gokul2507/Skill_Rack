a,b=list(input().strip()),list(input().strip())
c=0 
for i in range(min(len(a),len(b))):
    if a[i]==b[i]:
        c+=2 
        a[i]="*"
        b[i]="*"
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]!='*' and a[i]==b[j]:
            c+=1 
            b[j]='*'
            break
print(c)