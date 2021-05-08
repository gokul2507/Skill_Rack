#include <stdio.h>
void printPattern(int N)
{
    int x=1;
    for(int i=1;i<=N;i++){
        if(i%2){
            for(int j=0;j<i;j++){
                printf("%d ",x++);
            }
        }
        else{
            for(int j=0;j<i;j++) x++;
            for(int j=x-1;j>=x-i;j--) printf("%d ",j);
        }
        printf("\n");
    }
}
int main(){
    int n;
    scanf("%d",&n);
    printPattern(n);
}