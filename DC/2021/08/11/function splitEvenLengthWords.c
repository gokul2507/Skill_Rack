#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* splitEvenLengthWords(char *str)
{
    char *s=malloc(sizeof(char)*10001);
    char *t=strtok(str," ");
    while(t!=NULL){
        if(strlen(t)%2==0){char ch[1001];
        int l=0;
        for(int i=0;i<strlen(t);i++){
            if(i==strlen(t)/2) ch[l++]=' ';
            ch[l++]=t[i];
        }
        ch[l]='\0';
        strcat(s,ch);
        strcat(s," ");
        }
        else{
            strcat(s,t);
            strcat(s," ");
        }
        t=strtok(NULL," ");
    }
    return s;
}
int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    char *revisedStr = splitEvenLengthWords(str);
    printf("String: %s", revisedStr);
    return 0;
}