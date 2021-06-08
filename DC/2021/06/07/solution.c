#include <stdio.h>
#include <stdlib.h>

int ** getMatrixFromArrays(int m, int a1[], int n,int a2[])
{
    int s=sqrt(m+n);
    int **matrix=malloc(sizeof(int*)*s);
    for(int i=0;i<s;i++){
        matrix[i]=malloc(sizeof(int)*s);
    }
    int x=0,y=0;
    for(int i=0;i<m;i++){
        matrix[x][y]=a1[i];
        y++;
        if(y==s){
            x++;
            y=0;
        }
    }
    for(int i=0;i<n;i++){
        matrix[x][y]=a2[i];
        y++;
        if(y==s){
            x++;
            y=0;
        }
    }
    return matrix;
}

int main()
{
    int M, N;
    scanf("%d", &M);
    int arr1[M];
    for(int index = 0; index < M; index++)
    {
        scanf("%d", &arr1[index]);
    }
    scanf("%d", &N);
    int arr2[N], SIZE = sqrt(M+N);
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr2[index]);
    }
    int **newMatrix = getMatrixFromArrays(M, arr1, N, arr2);
    printf("Matrix:\n");
    for(int row = 0; row < SIZE; row++)
    {
        for(int col = 0; col < SIZE; col++)
        {
            printf("%d ", newMatrix[row][col]);
        }
        printf("\n");
    }
    return 0;
}
