#include <stdio.h>
void printValues(int a[], int n)
{
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(a[i]>a[j]){
                int t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
    for(int i=0;i<n;i+=2) printf("%d ",a[i]);
}
int main()
{
    int N;
    scanf("%d",&N);
    int arr[N];
    int index=0;
    for(; index < N; index++)
    {
        scanf("%d",&arr[index]);
    }
    printValues(arr,N);
    return 0;
}
