int samePositionBitCount(int N1, int N2)
{
    int count = 0;
    int N3 = N1 ^ N2;
    int max = N1 > N2 ? N1 : N2;
    while(N3 > 0||max)
    {
        if((N3 & 1) == 0)
        {
            count++;
        }
        max /= 2;
        N3 /= 2;
    }
    return count;
}
