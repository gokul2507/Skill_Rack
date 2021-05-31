input1 = input().strip().split(" ")
R,C = int(input1[0]), int(input1[1])
Matrix = [input().split() for j in range(R)]
for i in range(R): 
    for j in range(C):  
        Matrix[i][j] = int(Matrix[i][j])
Direction = input().strip()
count = 0
if(Direction == 'L'): 
    for i in range(R):    
        for j in range(C-1):  
            if(Matrix[i][j] == 1 and Matrix[i][j+1] == 0): 
                count += 1        
if(Direction == 'R'): 
    for i in range(R):   
        for j in range(1,C):
            if(Matrix[i][j-1] == 0 and Matrix[i][j] == 1): 
                count += 1  
if(Direction == 'B'):
    for i in range(R-1): 
        for j in range(C):  
            if(Matrix[i][j] == 1 and Matrix[i+1][j] == 0): 
                count += 1 
if(Direction == 'F'):  
    for i in range(1,R): 
        for j in range(C):        
            if(Matrix[i-1][j] == 0 and Matrix[i][j] == 1):  
                count += 1   
print(count)