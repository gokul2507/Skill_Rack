#include <stdio.h>
#include <stdlib.h>
void customToUpper(char s[], char c, char t)
{
    for(int i=0;i<strlen(s);i++){
        if(s[i]>=c && s[i]<=t){
            s[i]=toupper(s[i]);
        }
    }
}
int main(){
    char str[101],fromChar,toChar;
    scanf("%s\n%c %c",str,&fromChar,&toChar);
    customToUpper(str,fromChar,toChar);
    printf("Modified String: %s",str);
    return 0;
}