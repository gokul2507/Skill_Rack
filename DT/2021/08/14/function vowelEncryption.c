#include <stdio.h>
#include <stdlib.h>

char* vowelEncryption(char *str)
{
    char *t=malloc(sizeof(str)*10000);
    int c=0;
    for(int i=0;str[i]!='\0';i++){
        char q=tolower(str[i]);
        if(q=='a'||q=='e'||q=='i'||q=='o'||q=='u'){
            c++;
        }
        else{
            if(c)
            sprintf(t,"%s%d",t,c);
            sprintf(t,"%s%c",t,str[i]);
            c=0;
        }
    }
    if(c)
    sprintf(t,"%s%d",t,c);
    return t;
}

int main()
{
    char str[1001];
    scanf("%s", str);
    char *newStr = vowelEncryption(str);
    printf("Original String: %s\n", str);
    printf("Encrypted String: %s", newStr);
    return 0;
}
