#include<stdio.h>
#include<stdlib.h>

int main()
{
    int m,n,i,cnt=0;
    scanf("%d %d",&n,&m);
    for(i=0;n>0;i++){
        if(n%m==0){
            cnt++;
        }
        n=n/2;
    }
    printf("%d",cnt);

}