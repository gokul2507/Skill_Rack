#include<stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    scanf("%d",&a);
    int z[a];
    for(int i=0;i<a;i++)
    scanf("%d",&z[i]);
    int s=0,l=0;
    for(int i=0;i<a;i++){
        int t=z[i]+i,k=1;
        //printf("%d ",t-i);
        while(t<a){
            //printf("%d ",z[t]);
            t+=z[t];
            k++;
        }
        if(k>l){
            l=k;
            s=i;
        }
        //printf("\n");
    }
    l=s;
    printf("%d ",z[s]);
    s+=z[s];
    while(s<a){
        printf("%d ",z[s]);
        s+=z[s];
    }
}
