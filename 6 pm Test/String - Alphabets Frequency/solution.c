#include <stdio.h>
void printAlphabetCount(char s[])
{
    int a[128]={0};
    for(int i=0;i<strlen(s);i++){
        if(isalpha(s[i])) a[s[i]]+=1;
    }
    for(int i=0;i<128;i++){
        if(a[i]>0) printf("%c%d",(char)i,a[i]);
    }
}
int main(){
    int strval[201];
    scanf("%s",strval);
    printAlphabetCount(strval);
}