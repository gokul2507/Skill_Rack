#include<stdio.h>
#include<string.h>
void removeVowels(char strval[], int LENGTH){
    int l=0;
    for(int i=0;i<LENGTH;i++){
        char t=tolower(strval[i]);
        if(!(t=='a'|| t=='e'||t=='i'||t=='o'||t=='u'))
        strval[l++]=strval[i];
    }
    strval[l]='\0';
}
int main()
{
    char strval[100];
    scanf("%s",strval);
    removeVowels(strval,strlen(strval));
    printf("%s",strval);
    return 0;
}