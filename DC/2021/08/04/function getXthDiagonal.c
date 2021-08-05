#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray * getXthDiagonal(int r, int c, int m[r][c],int x){
    boundedArray *b= malloc(sizeof(boundedArray));
    b->arr=malloc(sizeof(int) * (r+c));
    b->SIZE=0;
    int R=r-1,C=0;
    for(int i=1;i<x;i++){
        if(R==0) C++;
        else R--;
    }
    while(R<r && C<c){
        b->arr[b->SIZE++]=m[R++][C++];
    }
    return b;
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
    boundedArray *bArr = getXthDiagonal(R, C, matrix, X);
    printf("Diagonal %d: ", X);
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}