input1 = input().strip().split(" ")
R,C = int(input1[0]), int(input1[1])
Matrix = [input().strip().split(" ") for j in range(R)]
numbers = [int(i) for i in input().strip().split(" ")]
pos = [R-1,-1]
 
def Snake():
    pos[0] = R-1
def Ladder():
    pos[0] -= 1
    
flag = 0

def func():
    if(pos[1] >= C):
        pos[0] -= 1
        pos[1] = pos[1] - C
 
    if(pos[1] < 0):
        pos[0] -= 1
        pos[1] = -pos[1] - 1
    
 
 
for i in numbers:
    flag += 1
    if(pos[0]%2 != 0):
        pos[1] += i
    else:
        pos[1] -= i
    
    func()
    if(Matrix[pos[0]][pos[1]] == "S"):
        Snake()
        func()
        func()
    if(Matrix[pos[0]][pos[1]] == "L"):
        Ladder()
        func()
        func()
    if(Matrix[pos[0]][pos[1]] == "S"):
        Snake()
        func()
        func()
    if(Matrix[pos[0]][pos[1]] == "L"):
        Ladder()
        func()
        func()
        
    if(pos[0] <= 0 and pos[1] <= 0):
        break
 
for i in numbers[:flag]:
    print(i,end = " ")