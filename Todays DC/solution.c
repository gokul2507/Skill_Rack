#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N;
    scanf("%d", &N);
    printf("%d", ( N >> 2  ) & 1 );
    return 0;
}
