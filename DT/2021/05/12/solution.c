#include<stdio.h>
#include<stdlib.h>

int main()
{
    int R,C,found=0;
    scanf("%d %d\n",&R,&C);
    char matrix[R][C],S[R*C];
    for(int row=0;row<R;row++){
        for(int col=0;col<C;col++){
            scanf("%c ",&matrix[row][col]);
        }
    }
    scanf("\n%s",S);
    for(int row=0;row<R;row++){
        for(int col=0;col<C;col++){
            if(matrix[row][col]==S[0] && found==0){
                found=1;
                int X=row,Y=col;
                for(int index=0;index<strlen(S);index++){
                    matrix[row][col]=S[index];
                    col++;
                    if(col==C){
                        row++;
                        col=0;
                        if(row==R){
                            row=0;
                        }
                    }
                }
            }
        }
    }
    for(int row=0;row<R;row++){
        for(int col=0;col<C;col++){
            printf("%c ",matrix[row][col]);
        }
        printf("\n");
    }
}