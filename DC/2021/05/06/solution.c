#include <stdio.h>
#include <stdlib.h>

int* mergeEven(int M, int *arr1, int N, int *arr2)
{
    int* arr=malloc(sizeof(int)*(M+N));
    int t=0,p=0;
    while(t+p<M+N){
        arr[p+t]=arr1[t];
        if(arr1[t]%2==0){
            arr[p+t+1]=arr2[p];
            p++;
        }
        t++;
    }
    return arr;
}
int main()
{
    int M, N;
    scanf("%d %d", &M, &N);
    int arr1[M], arr2[N];
    for(int index = 0; index < M; index++)
    {
        scanf("%d", &arr1[index]);
    }
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr2[index]);
    }
    int *mergedArr = mergeEven(M, arr1, N, arr2);
    printf("Array 1: ");
    for(int index = 0; index < M; index++)
    {
        printf("%d ", arr1[index]);
    }
    printf("\nArray 2: ");
    for(int index = 0; index < N; index++)
    {
        printf("%d ", arr2[index]);
    }
    printf("\nMerged Array: ");
    for(int index = 0; index < M+N; index++)
    {
        printf("%d ", mergedArr[index]);
    }
    return 0;
}