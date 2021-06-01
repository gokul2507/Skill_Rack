#include <stdio.h>
#include <stdlib.h>
void invertSubmatrix(int r, int c, int m[r][c], int sr, int sc, int k)
{
    sr--;
    sc--;
    for(int i=sr;i<sr+k;i++){
        for(int j=sc;j<sc+k;j++){
            if(m[i][j]==0) m[i][j]=1;
            else m[i][j]=0;
        }
    }
}
int main()
{
    int R, C, K, sRow, sCol;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    scanf("%d %d\n%d", &sRow, &sCol, &K);
    invertSubmatrix(R, C, matrix, sRow, sCol, K);
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            printf("%d ", matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
}
