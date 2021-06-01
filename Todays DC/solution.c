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
