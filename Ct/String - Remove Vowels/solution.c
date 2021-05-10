#include <stdio.h>
#include <string.h>
int* cellComplete(int cells[], int days) {
    int c=0;
    for(int i=0;i<days;i++){
        for(int j=0;j<8;j++){
            int p=(j==0)?0:c,n=(j==7)?0:cells[j+1];
            c=cells[j];
            cells[j]=(p==n)?0:1;
        }
    }
    return cells;
}
int main()
{
    char strval[100];
    scanf("%s",strval);
    removeVowels(strval,strlen(strval));
    printf("%s",strval);
    return 0;
}
