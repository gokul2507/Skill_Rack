#include <stdio.h> 
#include <stdlib.h> 
typedef struct BoundedArray { 
    int SIZE; 
    int *arr; 
} boundedArray;

boundedArray* integerToArray(int N)
{
    boundedArray *l=malloc(sizeof(boundedArray));
    l->arr=malloc(sizeof(int)*101);
    l->SIZE=0; 
    char a[101];
    int i=0;
    sprintf(a,"%d",N);
    if(a[0]=='-') i=1;
    for(;i<strlen(a);i++) l->arr[l->SIZE++]=a[i]-'0';
    return l;
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
