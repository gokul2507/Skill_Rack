#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;
boundedArray* removeMultiplesOfTen(int SIZE, int arr[])
{
    boundedArray ans=(struct BoundedArray)malloc(sizeof(struct BoundedArray));
    ans->arr=(int *)malloc(sizeof(int [SIZE]));
    ans->SIZE=0;
    for(int i=0;i<SIZE;i++){
        if(arr[i]%10)
        *(ans->arr+ans->SIZE++)=arr[i];
    }
    if(ans->SIZE==0){
        *(ans->arr+ans->SIZE++)=-1;
    }
    return ans;
}
int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    boundedArray *bArr = removeMultiplesOfTen(N, arr);
    printf("Old Array: ");
    for(int index = 0; index < N; index++)
    {
        printf("%d ", arr[index]);
    }
    printf("\nNew Array: ");
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}
