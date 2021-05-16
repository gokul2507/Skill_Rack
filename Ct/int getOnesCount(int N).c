int getOnesCount(int N)
{
    int count = 0;
    while(N != 0)
    {
        if(N & 1)
        {
            count++;
        }
        N /= 2;
    }
    return count;
}
