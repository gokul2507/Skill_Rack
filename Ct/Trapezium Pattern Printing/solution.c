#include <stdio.h>
#include <stdlib.h>
void printPattern(int N){
    int a=1,b=(N*N)+1,s=0;
    for(int l=N;l>=1;l--){
        for(int c=s;c>=1;c--){
        printf("-");
        }
        for(int i=1;i<=l;i++){
            if(i==l)
            printf("%d",a++);
            else
            printf("%d*",a++);
        }
        for(int i=1;i<=l;i++){
        printf("*%d",b++);
        }
    printf("\n");
        s+=2;
        b=(b-1)-((l-1)*2);
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    printPattern(n);
    return 0;
}