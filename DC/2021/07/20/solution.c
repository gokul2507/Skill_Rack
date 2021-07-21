#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, X, Y;
    scanf("%d %d %d", &N, &X, &Y);
    for(int val = 1; val <= N; val++)
    {
        if(val%X==0||val%Y==0)
        {
             continue;
        }
        printf("%d ", val);
    }
    return 0;
}

