#include <stdio.h>
void alternateSort(int arr[], int LENGTH)
{
    for(int i=0;i<LENGTH;i++){
        for(int j=i+1;j<LENGTH;j++){
            if(arr[i]>arr[j]){
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
        }
    }
    int a[LENGTH];
    for(int i=0;i<LENGTH;i++) a[i]=arr[i];
    int i=0,j=LENGTH-1,ctr=0;
    while(i<j){
        arr[ctr++]=a[j];
        arr[ctr++]=a[i];
        i++;
        j--;
    }
    if(LENGTH%2) arr[ctr]=a[i];
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
