#include<stdio.h>
#include <stdlib.h>
int main()
{
long int a,b;
scanf("%ld%ld",&a,&b);
while(a!=b)
{    
    if(a>b) 
    a=a-b;   
    else   
    b=b-a;
}
printf("%ld",a);
}
