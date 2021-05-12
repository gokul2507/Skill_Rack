#include<stdio.h>
#include <stdlib.h>
void pri(int a,int q){
    while(a--)
        printf("%d ",q++);
    printf("\n");
}
int main()
{
    int a;
    scanf("%d",&a);
    int t=1;
    for(int i=1;i<=a/2;i++){
        pri(a,t);
        t+=a+a;
    }
    if(a%2){
        pri(a,t);
    }
    for(int i=0;i<a/2;i++){
        t-=a;
        pri(a,t);
        t-=a;
    }
}
