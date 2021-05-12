#include <stdio.h>
void printSquare(int n)
{
    int c=1,x=1;
    while(x<=n){
        printf("%d ",x);
        c+=1;
        x=c*c;
    }
}
int main(){
    int n;
    scanf("%d",&n);
    printSquare(n);
}