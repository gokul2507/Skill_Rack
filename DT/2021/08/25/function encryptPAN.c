#include <stdio.h>
#include <stdlib.h>

int check(char x){
    x=tolower(x);
    return x=='a'||x=='e'||x=='i'||x=='u'||x=='o';
}
int find(char x,char *v){
    x=tolower(x);
    for(int i=0;v[i]!='\0';i++){
        if(x==v[i]){
            return strlen(v)-i-1;
        }
    }
}
char* encryptPAN(char *str)
{
    char *v="bcdfghjklmnpqrstvwxyz";
    char *s=malloc(sizeof(char)*1001);
    int sctr=0,pos;
    for(int i=0;str[i]!='\0';i++){
        if(check(str[i])==0 && isdigit(str[i])==0){
            s[sctr++]='*';
            if(isupper(str[i])){
                pos=find(str[i],v);
                s[sctr++]=v[pos];
            }
            else{
                s[sctr++]=str[i];
            }
        }
        else if(isdigit(str[i])){
            s[sctr++]=str[i];
        }
    }
    return s;
}

int main()
{
    char str[101];
    scanf("%s", str);
    char *encryptedPAN = encryptPAN(str);
    printf("Original PAN: %s\n", str);
    printf("Encrypted PAN: %s", encryptedPAN);
    return 0;
}