#include <stdio.h>
#include <stdlib.h>
void printPattern(int N)
{   
    int c=1;
    for(int i=1;i<=N;i++){
        if(i%2) for(int j=0;j<i;j++) printf("%d ",c++);
        else{
            for(int j=0;j<i;j++) c++;
            for(int j=c-1;j>=c-i;j--) printf("%d ",j);
        }
        printf("\n");
    }
}
int main()
{
    int N;
    scanf("%d",&N);
    printPattern(N);
}
