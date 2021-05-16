string=input().strip()
length=len(string)
mat=[["*" for _ in range(length)] for _ in range(length+1)]
def assign(row_start,col_start,i):
    l=0
    while l<length:
        mat[row_start][col_start]=string[l]
        l+=1
        row_start+=1
        col_start+=i
assign(0,0,1)
assign(1,0,1)
assign(1,-1,-1)
assign(0,-1,-1)
for i in mat:
    print(*i,sep='')
