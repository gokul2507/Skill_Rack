#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n,i,j,k=1;
    char c = 'a';
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++,k++)
        {
            if(i%2==n%2)
                printf("%c ",c);
            else
                printf("%d ",k);
            if(c=='z')
                c='a';
            else
                c++;
        }
        printf("\n");
    }
}