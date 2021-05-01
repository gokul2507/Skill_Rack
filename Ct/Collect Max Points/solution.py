a,b=map(int,input().split())
z=[list(map(int,input().split())) for _ in range(a)]
for j in range(1,b):   
    for i in range(a):   
        if i==0:           
            z[i][j]+=max(z[i][j-1],z[i+1][j-1]) 
        elif i==a-1:      
            z[i][j]+=max(z[i][j-1],z[i-1][j-1]) 
        else:          
            z[i][j]+=max(z[i-1][j-1],z[i][j-1],z[i+1][j-1])
print(max(list(zip(*z))[-1]))
