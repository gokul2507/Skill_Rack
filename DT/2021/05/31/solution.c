#include <stdio.h>
#include <stdlib.h>
int get(int R,int C,int z[R][C],int x,int y){
    if(x>=0 && x<R && y>=0 && y<C)
    return z[x][y];
    return 0;
}
int findSurroundingSum(int R, int C, int matrix[R][C], int x, int y)
{
    x-=1;
    y-=1;
    return get(R,C,matrix,x-1,y-1)+get(R,C,matrix,x-1,y)+get(R,C,matrix,x-1,y+1)+get(R,C,matrix,x,y-1)+get(R,C,matrix,x,y+1)+get(R,C,matrix,x+1,y-1)+get(R,C,matrix,x+1,y)+get(R,C,matrix,x+1,y+1);
}
int main()
{
    int R, C, X;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    scanf("%d", &X);
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            if(matrix[row][col] == X)
            {
                printf("%d ", findSurroundingSum(R, C, matrix, row+1, col+1));
            }
        }
    }
    return 0;
}
