#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,y,a,b;
    scanf("%d %d",&x,&y);
    int z[x][y];
    for(int i=0;i<x;i++)
    for(int j=0;j<y;j++)
    scanf("%d",&z[i][j]);
    scanf("%d %d",&a,&b);
    for(int i=0;i<y;i++)
    printf("%d ",z[a-1][i]*z[b-1][y-1-i]);
}