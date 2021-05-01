#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int a[n][n],x=1;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) a[i][j]=x++;
    for(int i=0;i<n;i++){
        if((i+1)%2){
            for(int j=0;j<n;j++) printf("%d ",a[i][j]);
            printf("\n");
        }
    }
    for(int i=n-1;i>=0;i--){
        if((i+1)%2==0){
            for(int j=0;j<n;j++) printf("%d ",a[i][j]);
            printf("\n");
        }
    }
}
