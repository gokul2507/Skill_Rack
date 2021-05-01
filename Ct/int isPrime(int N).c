int isPrime(int N)
{
    if(N<2)
    return 0;
    int divisor;
    int sqrtN = sqrt(N);
    for(divisor = 2; divisor <= sqrtN; divisor++)
    {
        if(N%divisor == 0)
        {
            return 0;
        }
    }
    return 1;
}
