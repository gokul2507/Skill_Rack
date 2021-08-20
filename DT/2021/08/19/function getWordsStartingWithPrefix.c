#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;

} boundedArray;
 
boundedArray* getWordsStartingWithPrefix(char *str, char *prefix)
{
    boundedArray * ans = malloc(sizeof(boundedArray));
    char * token = strtok(str," ");
    ans->SIZE = 0 ;
    ans->words = malloc(sizeof(char*)*1000);
    int prefixLength = strlen(prefix);
    while(token){
        char temp[100];
        strcpy(temp,token);
        temp[prefixLength] = 0;
        if(strcmp(temp,prefix)==0){
            ans->words[ans->SIZE] = malloc(1000);
            strcpy(ans->words[ans->SIZE++],token);
        }
        token = strtok(NULL," ");
    }
    if(!ans->SIZE){
        ans->words[0] = malloc(sizeof(100));
        strcpy(ans->words[ans->SIZE++] ,"-1");
    }
    return ans;
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