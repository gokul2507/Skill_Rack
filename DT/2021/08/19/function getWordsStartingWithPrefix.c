#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;

} boundedArray;
 
boundedArray* getWordsStartingWithPrefix(char *str, char 
    *prefix)
{

}

int main()
{
    char str[10001], prefix[101];
    scanf("%[^\n]\n%s", str, prefix);
    boundedArray *bArr = getWordsStartingWithPrefix(str, prefix);
    printf("Words starting with prefix %s:\n", prefix);
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s\n", bArr->words[index]);
    }
    return 0;

}