void toggleVowelCase(char str[])
{
    for(int index=0; str[index]!='\0'; index++)
    {
        if(isVowel(str[index]))
        {
            printf("%c",toggle(str[index]));
        }
        else
        {
            printf("%c",str[index]);
        }
    }
}
