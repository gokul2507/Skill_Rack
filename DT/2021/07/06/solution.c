#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;
 
boundedArray* concatEveryTwoWords(char str[])
{
    
}
int main()
{
    char str[1001];
    scanf("%[^\n\r]", str);

    boundedArray *bArr = concatEveryTwoWords(str);
    printf("Words:\n");
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s\n", bArr->words[index]);
    }
    return 0;
}
