#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    long long int *arr;
} boundedArray;
 
boundedArray* concatEveryTwoIntegers(int SIZE, int *arr)
{
    boundedArray *bArr = malloc(sizeof(boundedArray));
    bArr->arr=malloc(sizeof(long long int)*(SIZE/2));
    bArr->SIZE=0;
    for(int index=0;index<SIZE;index+=2){
        char numStr[101];
        sprintf(numStr,"%d%d",arr[index],arr[index+1]);
        bArr->arr[bArr->SIZE++]=atoll(numStr);
    }
    return bArr;
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