#include <stdio.h>
void alternateSort(int arr[], int LENGTH)
{
    //selection sort
    for(int i=0;i<LENGTH;i++){
        int t=i;
        for(int j=i+1;j<LENGTH;j++){
            if(i%2){
                if(arr[t]>arr[j])
                t=j;
            }
            else{
                if(arr[t]<arr[j])
                t=j;
            }
        }
        if(i!=t){
            arr[t]+=arr[i];
            arr[i]=arr[t]-arr[i];
            arr[t]=arr[t]-arr[i];
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

    alternateSort(arr,N);

    for(index = 0; index < N; index++)
    {
        printf("%d ",arr[index]);
    }
}
