r,c=map(int,input().split())
count=0 
while (r>0 or c>0):
    if r%2!=c%2:
        count+=1 
    r//=2 
    c//=2 
print(count)
