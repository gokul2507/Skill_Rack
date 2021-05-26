#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;
boundedArray* getColumn(int R, int C, int matrix[][C], int K)
{
boundedArray *bArr=malloc(sizeof(boundedArray));
bArr->arr=malloc(sizeof(int)*R);
bArr->SIZE=0;
for(int row=0;row<R;row++){
    bArr->arr[bArr->SIZE++]=matrix[row][K-1];
}
return bArr;
}
int main()
{
    int R, C, K;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    scanf("%d", &K);
    boundedArray *bArr = getColumn(R, C, matrix, K);
    printf("Column %d: ", K);
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}
