#include <stdio.h>
#include <stdlib.h>
typedef struct BoundedArray{
    int SIZE;
    int *arr;
}   boundedArray;
boundedArray* getThreeOrFourDigits(int SIZE, int arr[])
{
    boundedArray *t=malloc(sizeof(boundedArray *));
    t->SIZE=0;
    t->arr=malloc(sizeof(int [SIZE]));
    for(int i=0;i<SIZE;i++){
        if(arr[i]>99 && arr[i]<10000){
            t->arr[t->SIZE]=arr[i];
            t->SIZE++;
        }
    }
    if(t->SIZE==0){
        t->SIZE=1;
        t->arr[0]=-1;
    }
    return t;
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
    boundedArray *bArr = getThreeOrFourDigits(N, arr);
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