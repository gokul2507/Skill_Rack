#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    char s[11],s1[11];
    scanf("%s",s);
    int l=strlen(s);
    for(int i=l-1,j=0;i>=0,j<l;i--,j++) s1[j]=s[i];
    printf("%d",atoi(s)-atoi(s1));
}
