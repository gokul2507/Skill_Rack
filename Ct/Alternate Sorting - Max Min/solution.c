#include <stdio.h>
void alternateSort(int arr[], int LENGTH)
{
    for(int i=0;i<LENGTH;i++){
        int x=i;
        for(int j=i+1;j<LENGTH;j++){
            int s=arr[x]-arr[j];
            if(i%2==0)
            s=arr[j]-arr[x];
            if(s>0) x=j;
        }
        if(i!=x){
            arr[i]+=arr[x];
            arr[x]=arr[i]-arr[x];
            arr[i]-=arr[x];
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
