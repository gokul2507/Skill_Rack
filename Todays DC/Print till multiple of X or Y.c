#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, X, Y, val;
    scanf("%d %d %d", &N, &X, &Y);
    for(int ctr = 1; ctr <= N; ctr++)
    {
        scanf("%d", &val);
        for(int printVal = val; printVal >= 1; printVal--)
        {
            if(printVal%X==0 || printVal%Y==0){
             printf("%d",printVal);
             break;
                }
        else printf("%d ",printVal);
        }
        printf("\n");
    }
    return 0;
}

