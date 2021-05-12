#include <stdio.h>
void arraySplitSort(int arr[], int N, int K)
{
    for(int i=0;i<K;i++){
        for(int j=i+1;j<K;j++){
            if(arr[i]>arr[j]){
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
        }
    }   
    for(int i=K;i<N;i++){
        for(int j=i+1;j<N;j++){
            if(arr[i]<arr[j]){
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
        }
    }
}
int main()
{
    int N;
    scanf("%d",&N);
    int arr[N];

    int index;
    for(index = 0; index < N; index++)
    {
        scanf("%d",&arr[index]);
    }

    mergesort(arr,0,N-1);

    for(index = 0; index < N; index++)
    {
        printf("%d ",arr[index]);
    }
}
