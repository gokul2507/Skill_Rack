#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;
_Bool isvow(char c){
    c=tolower(c);
    return c=='a' || c=='e' || c=='o' || c=='u' || c=='i';
}
boundedArray* getWordsStartingWithVowel(char str[])
{
    boundedArray *ptr=malloc(sizeof(boundedArray));
    ptr->words=(char**)malloc(1000*sizeof(char*));
    for(int i=0; i<1000; i++)
    ptr->words[i]=(char*)malloc(1000);
    ptr->SIZE=0;
    char *s=strtok(str," ");
    while(s){
        if(isvow(s[0]))
        strcpy(ptr->words[ptr->SIZE++],s);
        s=strtok(0," ");
    }
    if(!ptr->SIZE)
    ptr->words[ptr->SIZE++]="-1";
    return ptr;
}
int main()
{
    char str[1001];
    scanf("%[^\n]", str);

    boundedArray *bArr = getWordsStartingWithVowel(str);

    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s\n", bArr->words[index]);
    }
    return 0;
}