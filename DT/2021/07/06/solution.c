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
    boundedArray *bArr=malloc(sizeof(boundedArray));
    bArr->words=malloc(sizeof(int*)*1001);
    for(int index=0;index<1001;index++){
        bArr->words[index]=malloc(sizeof(char)*1001);
    }
    bArr->SIZE=0;
    char *word=strtok(str," ");
    int flag=1;
    while(word!=NULL){
        if(flag){
            strcpy(bArr->words[bArr->SIZE],word);
            flag^=1;
        }
        else
        {
            strcat(bArr->words[bArr->SIZE++],word);
            flag^=1;
        }
        word=strtok(NULL," ");
    }
    return bArr;
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