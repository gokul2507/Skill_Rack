#include <stdio.h>
#include <stdlib.h>
 
int countShoePairs(int n, int *arr)
{
    int a[1001]={0},s[101],sc=0,c=0;
    for(int i=0;i<n;i++){
         if(a[arr[i]]==0) s[sc++]=arr[i];
         a[arr[i]]+=1;
    }
    for(int i=0;i<sc;i++){
        c+=a[s[i]]/2;
    }
    return c;
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
    printf("%d", countShoePairs(N, arr));
    return 0;
}