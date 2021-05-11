#include <stdio.h>

void main()
{
    int N, MAX_CACHE_SIZE;
    scanf("%d%d",&MAX_CACHE_SIZE,&N);
    int arr[N];
    int index;
    for(index = 0; index < N; index++)
    {
        scanf("%d",&arr[index]);
    }

    int *ptr = arr;
    printf("%d",lruCountMiss(MAX_CACHE_SIZE,ptr,N));

}
