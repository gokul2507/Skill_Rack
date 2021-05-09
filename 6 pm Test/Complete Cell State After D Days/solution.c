#include <stdio.h>
#define CELLSCOUNT 8
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
int main() {
        int cells[CELLSCOUNT];

        //Accept the input for the cell values
        int index;
        for (index = 0; index < CELLSCOUNT; index++) {
            scanf("%d",&cells[index]);
        }

        int DAYS;
        scanf("%d",&DAYS); //Get the number of days
        int* modified = cellComplete(cells, DAYS);

        //Print the modified cell values
        for (index = 0; index < CELLSCOUNT; index++) {
            printf("%d ",modified[index]);
        }
    }
