R,C=map(int,input().split())
matrix=[input().split() for row in range(R)]
S=input().strip()
for X in range(1,R+1):
    for Y in range(1,C+1):
        for row in range(R-X+1):
            for col in range(C-Y+1):
                subStr=""
                for sRow in range(row,row+X):
                    for sCol in range(col,col+Y):
                        subStr+=matrix[sRow][sCol]
                if subStr==S:
                    for sRow in range(row,row+X):
                        for sCol in range(col,col+Y):
                            print(matrix[sRow][sCol],end=" ")
                        print()
                    exit()