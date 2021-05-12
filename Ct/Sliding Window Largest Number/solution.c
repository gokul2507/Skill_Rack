#include<stdio.h>
#include<stdlib.h>
int t;
void print(int z[]){
    int p=z[0];
    for(int i=1;i<t;i++)
    if(p<z[i])
    p=z[i];
    printf("%d ",p);
}
int main()
{
    int n;
    scanf("%d %d",&t,&n);
    int z[t];
    for(int i=0;i<n;i++){
        scanf("%d",&z[i%t]);
        if(i>=t-1)
        print(z);
    }
}
