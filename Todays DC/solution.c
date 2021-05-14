#include <stdio.h>
#include <stdlib.h>

void printMatrix(int R, int C, int matrix[][C])
{
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            printf("%d ", matrix[row][col]);
        }
        printf("\n");
    }
} 

int** addTwoMatrices(int R, int C, int *matrix1, int *matrix2)
{
    int **mat=malloc(sizeof(int *)*R);
int ind=0;
for(int i=0;i<R;i++){
    mat[i]=malloc(sizeof(int)*C);
    for(int j=0;j<C;j++){
        mat[i][j]=*(matrix1+ind)+*(matrix2+ind);
        ind++;
    }
}
return mat;
}

int main()
{
    int R, C;
    scanf("%d %d", &R, &C);
    int matrix1[R][C], matrix2[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix1[row][col]);
        }
    }
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix2[row][col]);
        }
    }
    int **resultMatrix = addTwoMatrices(R, C, matrix1, matrix2);
    printf("Matrix 1:\n");
    printMatrix(R, C, matrix1);
    printf("Matrix 2:\n");
    printMatrix(R, C, matrix2);
    printf("Matrix Sum:\n");
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            printf("%d ", resultMatrix[row][col]);
        }
        printf("\n");
    }
    return 0;
}