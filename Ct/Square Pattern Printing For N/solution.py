a=int(input()) 
b=[[0 for i in range(a)]for i in range(a)] 
c=1 
for i in range(a): 
    b[0][i]=c  
    c+=1 
for i in range(1,a): 
    b[i][0]=b[i-1][1]  
    for j in range(1,a-1): 
        b[i][j]=b[i-1][j-1]+b[i-1][j+1]  
    b[i][a-1]=b[i-1][a-2] 
for i in b: 
    print(*i)