#include<stdio.h>
#include<stdlib.h>

int main()
{
    int R,C;
    scanf("%d %d",&R,&C);
    int matrix[R][C];
    long long int sum=0;
    for(int row=0;row<R;row++){
        for(int col=0;col<C;col++){
            scanf("%d ",&matrix[row][col]);
        }
    }
    for(int col=0;col<C;col++){
        long long int num1=0,num2=0;
        for(int row=0;row<R;row++){
            num1=(num1*2)+matrix[row][col];
            num2=(num2*2)+matrix[R-row-1][col];
        }
        if(num1>num2){
            sum+=num1;
        }
        else
        {
            sum+=num2;
        }
    }
    printf("%lld",sum);
}