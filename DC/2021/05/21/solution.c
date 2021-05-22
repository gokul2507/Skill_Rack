#include<stdio.h>
#include<stdlib.h>

int main()
{
    int arr[1001],k=0,temp,flag=0;
    char ch;
    while(scanf("%d%c",&temp,&ch)>0)
    {
        if(ch==' ')
        {
            arr[k++] = temp;
            flag=1;
        }
        else
        {
            arr[k++] = temp;
        }
    }
    if(flag==0)
    {
        for(int i=k-1;i>=0;i--)
        {
            printf("%d ",arr[i]);
        }
    }
    else
    {
        for(int i=k-1;i>=0;i--)
        {
            printf("%d\n",arr[i]);
        }
    }

}