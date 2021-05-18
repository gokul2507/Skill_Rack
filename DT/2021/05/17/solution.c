#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,i,j,y,a[55][55],z,t,u;
    scanf("%d %d",&x,&y);
    for(i=0;i<x;i++)
    for(j=0;j<y;j++)
    scanf("%d ",&a[i][j]);
    scanf("%d ",&z);
    t=z;
for(i=z-1;i>=0;i--)
{
    for(j=0;j<y;j++)
    {
    u=a[i][j];
    if(t<x)
    u+=a[t][j];
    printf("%d ",u);
    }
    printf("\n");
    t++;
}
while(t<x)
{
    for(j=0;j<y;j++)
    printf("%d ",a[t][j]);
    printf("\n");
    t++;
}

}