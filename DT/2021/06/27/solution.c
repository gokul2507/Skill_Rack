#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int **matrix;
} boundedArray;
 
boundedArray* getLargestSquareMatrix(int R, int C, int matrix[R][C]
    , int sRow, int sCol)
{
    
}
int main()
{
    int R, C;
    scanf("%d %d", &R, &C);
    int matrix[R][C], sRow, sCol;
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    scanf("%d %d", &sRow, &sCol);

    boundedArray *bArr = getLargestSquareMatrix(R, C, matrix, sRow, sCol);

    printf("Square Matrix:\n");
    for(int row = 0; row < bArr->SIZE; row++)
    {
        for(int col = 0; col < bArr->SIZE; col++)
        {
            printf("%d ", bArr->matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
}
