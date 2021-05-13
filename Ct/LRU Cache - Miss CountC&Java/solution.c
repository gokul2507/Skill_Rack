#include <stdio.h>
int lruCountMiss(int n, int *l, int len)
{
    int s[n];
    int c=0;
    for(int i=0;i<n;i++) s[i]=-1;
    for(int i=0;i<len;i++){
        for(int j=0;j<n;j++){
            if(l[i]==s[j]){
                for(int k=j;k<n-1;k++) s[k]=s[k+1];
                s[n-1]=l[i];
                break;
            }
            else if(j==(n-1)){
                for(int m=0;m<n;m++) s[m]=s[m+1];
                s[n-1]=l[i];
                c++;
            }
        }
    }
    return c;
}
void main()
{
    int N, MAX_CACHE_SIZE;
    scanf("%d%d",&MAX_CACHE_SIZE,&N);
    int arr[N];
    int index;
    for(index = 0; index < N; index++)
    {
        scanf("%d",&arr[index]);
    }

    int *ptr = arr;
    printf("%d",lruCountMiss(MAX_CACHE_SIZE,ptr,N));

}
