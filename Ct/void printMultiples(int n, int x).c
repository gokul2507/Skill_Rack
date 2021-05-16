void printMultiples(int n, int x)
{
    for(int ctr = 1; ctr <= n; ctr++)
    {
        if(ctr%x == 0)
        {
            printf("%d ", ctr);
        }
    }
}
