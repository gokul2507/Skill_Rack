#include<stdio.h>
#include <stdlib.h>
int main()
{
    int a,b,i,j,t,s;
    scanf("%d %d",&a,&b);
    for(i=0;i<a;i++){
        t=0; 
        for(j=0;j<b;j++)  
        {     
            scanf("%d",&s); 
            t+=s; 
        } 
        printf("%d\n",t);
    }
}