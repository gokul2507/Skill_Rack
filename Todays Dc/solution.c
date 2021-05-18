#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;
boundedArray* integerToArray(int N)
{
    if(N<0)
    N*=-1;
    int l=0,temp=N;
    while(temp){
        l++;
        temp/=10;
    }
    boundedArray *t=malloc(sizeof(int)*(l+2));
    t->SIZE=0;
    t->arr=malloc(sizeof(int)*l);
    for(int i=l-1;i>=0;i--){
        *(t->arr+i)=N%10;
        N/=10;
        t->SIZE++;
    }
    return t;
}
int main()
{
    int N;
    scanf("%d", &N);
    boundedArray *bArr = integerToArray(N);
    printf("Array: ");
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}