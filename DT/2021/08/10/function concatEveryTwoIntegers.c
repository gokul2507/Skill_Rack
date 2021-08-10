#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    long long int *arr;
} boundedArray;
 
boundedArray* concatEveryTwoIntegers(int SIZE, int *arr)
{
    
}

int main()
{
    int SIZE;
    scanf("%d", &SIZE);
    int arr[SIZE];
    for(int index = 0; index < SIZE; index++)
    {
        scanf("%d", &arr[index]);
    }
    boundedArray *bArr = concatEveryTwoIntegers(SIZE, arr);
    printf("Array: ");
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%lld ", bArr->arr[index]);
    }
    return 0;
}