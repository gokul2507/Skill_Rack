#include<stdio.h>
#include<stdlib.h>
int ch(int a[][30],int x,int y)
{
    int i,j;
    for(i=0;i<x;i++)
    for(j=0;j<y;j++)
    if(a[i][j]==1)
    return 1;
    return 0;
}
int main()
{
    int x,y,i,j,k,s=0;
    int a[30][30]={0};
    char c;
    scanf("%d %d\n",&x,&y);
    for(i=0;i<x;i++,scanf("\n"))
    for(j=0;j<y;j++)
    {
        scanf("%c ",&c);
        if(c=='*')
        a[i][j]=0;
        else
        a[i][j]=1;
    }
    k=1;
    while(ch(a,x,y))
    {
    if(k%2==1)
    {
        for(i=0;i<x;i++)
        {
            for(j=y-1;j>=0;j--)
            {
                if(a[i][j]==1)
                {
                    if(a[i-1][j]==1||a[i+1][j]==1)
                    {
                    break;
                    }
                    else
                {
                    if(a[i][j-1]==1)
                    a[i][j-1]=0;
                    a[i][j]=0;
                    break;
                }
        
                }
            }
        }
    }
    else
    {
        for(j=0;j<y;j++)
        {
            for(i=x-1;i>=0;i--)
            {
                if(a[i][j]==1)
                {
                    if(a[i][j-1]==1||a[i][j+1]==1)
                    break;
                    else
                    {
                        if(a[i-1][j]==1)
                        a[i-1][j]=0;
                        a[i][j]=0;
                        break;
                    }
                }
            }
        }
        
    }
    k++;
    /*
    for(i=0;i<x;i++,printf("\n"))
    for(j=0;j<y;j++)
    printf("%d ",a[i][j]);*/
    }
    printf("%d",k-1);
    

}