#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;
 
boundedArray* customSplit(char *str, char delimiter)
{
    boundedArray *n=malloc(sizeof(boundedArray));
    n->words=malloc(sizeof(char *)*1001);
    for(int i=0;i<1001;i++){
        n->words[i]=malloc(sizeof(char)*1001);
    }
    n->SIZE=0;
    char *p=strtok(str,&delimiter);
    while(p!=NULL){
        strcpy(n->words[n->SIZE++],p);
        p=strtok(NULL,&delimiter);
    }
    return n;
}
int main()
{
    char str[1001], delimiter;
    scanf("%s\n%c", str, &delimiter);
    boundedArray *bArr = customSplit(str, delimiter);
    printf("Words:\n");
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s\n", bArr->words[index]);
    }
    return 0;
}
