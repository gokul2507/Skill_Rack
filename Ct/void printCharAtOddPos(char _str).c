void printCharAtOddPos(char *str)
{
    int index=0,len=strlen(str);
    while(index < len)
    {
        printf("%c", str[index]);
        index+=2;
    }
}
