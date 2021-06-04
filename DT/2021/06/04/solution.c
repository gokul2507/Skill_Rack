#include<stdio.h>

typedef struct BoundedArray
{
    int SIZE;
    double *arr;
} boundedArray;
 
boundedArray* getAverages(int SIZE, int arr[])
{
 
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
    boundedArray *ptr = getAverages(N, arr);
    for(int index = 0; index < ptr->SIZE; index++)
    {
        printf("%.2lf ", ptr->arr[index]);
    }
  
}