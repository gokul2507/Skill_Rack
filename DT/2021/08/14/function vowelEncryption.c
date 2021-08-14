#include <stdio.h>
#include <stdlib.h>
 
char* vowelEncryption(char *str)
{
    
}

int main()
{
    char str[1001];
    scanf("%s", str);
    char *newStr = vowelEncryption(str);
    printf("Original String: %s\n", str);
    printf("Encrypted String: %s", newStr);
    return 0;
}