#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int customCompare(char s1[],char s2[]){
    char a[101],b[101];
    int c1=0,c2=0;
    for(int i=0;i<strlen(s1);i++){
        if(s1[i]>=65 && s1[i]<=90) a[c1++]=s1[i];
    }
    a[c1]='\0';
    for(int i=0;i<strlen(s2);i++){
        if(s2[i]>=65 && s2[i]<=90) b[c2++]=s2[i];
    }
    b[c2]='\0';
    return strcmp(a,b)==0;
}
int main()
{
    char str1[101], str2[101];
    scanf("%s\n%s", str1, str2);
    printf("%d", customCompare(str1, str2));
    return 0;
}
