#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;
 
boundedArray* getEvenLengthWords(char s[])
{
    boundedArray *b=malloc(sizeof(boundedArray));
    b->words=malloc(sizeof(char*)*1001);
    for(int i=0;i<1001;i++) b->words[i]=malloc(sizeof(char)*1001);
    b->SIZE=0;
    char *t=strtok(s," ");
    while(t!=NULL){
        if(strlen(t)%2==0) strcpy(b->words[b->SIZE++],t);
        t=strtok(NULL," ");
    }
    if(b->SIZE==0) strcpy(b->words[b->SIZE++],"-1");
    return b;
}
int main()
{
    char str[1001];
    scanf("%[^\n]", str);

    boundedArray *bArr = getEvenLengthWords(str);
    printf("Even Length Words:\n");
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s\n", bArr->words[index]);
    }
    return 0;
}
