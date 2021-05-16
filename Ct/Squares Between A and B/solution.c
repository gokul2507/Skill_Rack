#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int x;
int squar(int n){
    float t=sqrt(n);
    if((int)t==t)
    return 1;
    return 0;
}
int main()
{
    int y;
    scanf("%d %d",&x,&y);
    int f=0;
    while(x<=y){
        if(squar(x)){
            if(f)
            printf(",");
            printf("%d",x);
            f=1;
        }
        x++;
    }
}
