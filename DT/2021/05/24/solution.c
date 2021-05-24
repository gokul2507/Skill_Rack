#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

int isunique(int x){
    int a[10]={0};
    while(x){
        if(a[x%10]){
            return 0;
        }
        a[x%10]=1;
        x/=10;
    }
    return 1;
}
boundedArray* getIntegersWithUniqueDigits(int SIZE, int arr[])
{
    boundedArray *ans=(struct BoundedArray*)malloc(sizeof(struct BoundedArray));
    ans->arr=malloc(sizeof(int)*SIZE);
    ans->SIZE=0;
    for(int i=0;i<SIZE;i++){
        if(isunique(arr[i])){
            ans->arr[ans->SIZE++]=arr[i];
        }
    }
    if(ans->SIZE==0){
        ans->SIZE=1;
        ans->arr[0]=-1;
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
    boundedArray *bArr = getIntegersWithUniqueDigits(N, arr);
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