#include<stdio.h>
#include <stdlib.h>

int main()
{
    char str[101];
    scanf("%s", str);
    int X = 0;
    for(int index = 0; str[index] != '\0'; index++)
    {
        X =  X|(1<<(str[index]-97));
    }
    printf("%d", X);
    return 0;
}