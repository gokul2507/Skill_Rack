r,c=map(int,input().split())
a=[input().split() for i in range(r)]
count=0
for i in range(1,r-1): 
    for j in range(1,c-1):   
        if(a[i][j]=='-' and (a[i-1][j+1]=='*' or a[i-1][j-1]=='*' or a[i+1][j+1]=='*' or a[i+1][j-1]=='*')):   
            count+=1
for j in range(1,c-1):  
    if a[0][j]=='-' and (a[1][j+1]=='*' or a[1][j-1]=='*'):     
        count+=1  
    if a[r-1][j]=='-' and (a[r-2][j+1]=='*' or a[r-2][j-1]=='*'):   
        count+=1 
for i in range(1,r-1):
    if a[i][0]=='-' and (a[i+1][1]=='*' or a[i-1][1]=='*'):     
        count+=1    
    if a[i][c-1]=='-' and (a[i+1][c-2]=='*' or a[i-1][c-2]=='*'):   
        count+=1 
if a[0][0]=='-' and a[1][1]=='*':count+=1
if a[0][c-1]=='-' and a[1][c-2]=='*':count+=1 
if a[r-1][0]=='-' and a[r-2][1]=='*':count+=1
if a[r-1][c-1]=='-' and a[r-2][c-2]=='*':count+=1
print(count)
