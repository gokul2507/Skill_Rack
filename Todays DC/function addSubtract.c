#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int addSubtract(char *s)
{
    int ctr=0,sum=0;
    s=s+1;
    s[strlen(s)-1]='\0';
    char *t=strtok(s,")(");
    while(t!=NULL){
        int temp;
        sscanf(t,"%d",&temp);
        if(ctr==0) sum=temp;
        else{
            if(ctr%2) sum+=temp;
            else sum-=temp;
        }
        t=strtok(NULL,")(");
        ctr++;
    }
    return sum;
}

int main()
{
    char str[1001];
    scanf("%s", str);
    printf("%d", addSubtract(str));
    return 0;
}