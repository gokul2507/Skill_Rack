#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, X, Y, val;
    scanf("%d%d%d", &N, &X, &Y);
    for(int ctr = 1; ctr <= N; ctr++)
    {
        scanf("%d", &val);
        for(int printVal = 1; printVal<=val ; printVal++)
        {
            if( printVal>=X && printVal<=Y )
            {
                continue;
            }
            printf("%d ", printVal);
        }
        printf("\n");
    }
    return 0;
}