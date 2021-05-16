#include<stdio.h>
#include <stdlib.h>

int main()
{
int i=0,j,k=0,l,n,front,back,time1,frontditch,backditch;
scanf("%d",&n);
for(l=0;l<n;l++)
{
scanf("%d%d%d%d%d",&front,&back,&time1,&frontditch,&backditch);
backditch=-backditch;
if(front==back&&frontditch==front)
printf("%d F",(front*time1));
else if(front>frontditch)
printf("%d F",time1*frontditch);
else if(front==back&&frontditch!=front&&front<frontditch)
printf("No Ditch");
else if(back>-(backditch))
printf("%d B",time1*backditch);
else
{
    for(j=0;j<100000;j++)
    {
        if(j%2==0)
        {
        i=i+front;
        k=k+front;
       // printf("%d %d \n",i,k);
        }
        else
        {
        i=i-back;
        k=k+back;
       // printf("%d %d \n",i,k);
        }
        if(i>=frontditch||i<=backditch)
        {
        break;
        }
    }
if(i<0&&i==(backditch))
printf("%d B",((k)*time1));
else if(i<0)
printf("%d B",((k-1)*time1));
else if(i>0&&i==frontditch)
printf("%d F",(k*time1));
else
printf("%d F",((k-1)*time1));
i=0;k=0;
}
printf("\n");
}
}
