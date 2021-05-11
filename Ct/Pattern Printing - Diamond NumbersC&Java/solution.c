#include <stdio.h>
void zero(int n){
    while(n--)
    printf("0 ");
}
void num(int n){
    printf("%d ",n);
}
void printPattern(int N)
{
    int l=1,r=(N-1)*4,x=-1;
    for(int i=1;i<N+N;i++){
        zero(abs(N-i));
        if(i==1 ||i==N+N-1)
        num(l++);
        else{
            num(l++);
            zero(x);
            num(r--);
        }
        if(N-i>0)
        x+=2;
        else
        x-=2;
        zero(abs(N-i));
        printf("\n");
    }
    
}
int main()
{
    int N;
    scanf("%d",&N);
    printPattern(N);
    return 0;
}