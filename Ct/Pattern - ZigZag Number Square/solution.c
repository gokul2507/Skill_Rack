#include <stdio.h>
void printPattern(int n)
{   int c=1;
    for(int i=1;i<=n;i++){
        if(i%2){
            for(int j=0;j<n;j++) printf("%d ",c++);
        }
        else{
            int x=c+n-1;
            for(int j=x;j>=c;j--) printf("%d ",j);
            c=x+1;
        }
        printf("\n");
    }
}
int main(){
    int n;
    scanf("%d",&n);
    printPattern(n);
    return 0;
}