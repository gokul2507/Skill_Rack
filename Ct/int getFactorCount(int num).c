int getFactorCount(int num)
{
    int c=2;
    for(int i=2;i<=num/2;i++){
        if(num%i==0)
        c++;
    }
    return c;
}
