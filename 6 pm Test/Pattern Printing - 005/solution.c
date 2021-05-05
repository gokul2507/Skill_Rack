#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a;
    scanf("%d",&a);
    for(int i=1;i<=a;i++)
    {
        for(int j=0;j<i;j++)
        printf("%d",i);
        printf("\n");
    }
    for(int i=a;i>=1;i--)
    {
        for(int j=0;j<i;j++)
        printf("%d",i);
        printf("\n");
    }
}