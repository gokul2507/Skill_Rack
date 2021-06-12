s=0
for i in zip(input().strip(),input().strip()):
    i,j=sorted([int(i[0]),int(i[1])])
    s+=min(j-i,i+1+(9-j))
print(s)