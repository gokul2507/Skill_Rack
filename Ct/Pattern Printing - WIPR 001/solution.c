#include <stdio.h>
#include <stdlib.h>
void printPattern(int N)
{
    int l=1,n=1;
    while(l<=N){
        if(l%2)
        for(int i=0;i<l;i++)
        printf("%d ",n++);
        else
        for(int i=0;i<l;i++){
            printf("%d ",-1-i-i+l+n++);
        }
        printf("\n");
        l++;
    }
}
int main()
{
    int N;
    scanf("%d",&N);
    printPattern(N);
}
