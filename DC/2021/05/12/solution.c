#include <stdio.h>
#include <stdlib.h>
typedef struct BoundedArray{
    int SIZE;
    int *arr;
}   boundedArray;
int count(int n){
    int c=0;
    while(n>0){
        c++;
        n/=10;
    }
    return c;
}
boundedArray* getThreeOrFourDigits(int SIZE,int arr[]){
    boundedArray *b=malloc(sizeof(boundedArray));
    b->arr=malloc(sizeof(int)*SIZE);
    b->SIZE=0;
    for(int i=0;i<SIZE;i++){
        if(count(arr[i])==3 || count(arr[i])==4) b->arr[b->SIZE++]=arr[i];
    }
    if(b->SIZE==0){
        b->SIZE=1;
        b->arr[0]=-1;
    }
    return b;
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
