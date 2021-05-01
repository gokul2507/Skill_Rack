int matrixSum(int *matrix,int m,int n)
{
    int i,j,sum=0;
    for(i=0; i<m; i++)
    {
        for(j=0; j<n; j++)
        {
            sum+=*(matrix+i*n+j);
        }
    }
    return sum;
}
