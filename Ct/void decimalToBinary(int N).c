void decimalToBinary(int N)
{
    if(N > 0)
    {
        decimalToBinary(N/2);
        printf("%d",N%2);
    }
}
