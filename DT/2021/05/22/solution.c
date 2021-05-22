#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    int x,y,t=0;
    scanf("%d %d\n",&x,&y);
    char z[x][y][4],l[x][y][4];
    for(int i=0;i<x;i++){
        for(int j=0;j<y;j++){
            scanf("%s ",z[i][j]);
        }
    }
    for(int i=0;i<x;i++){
        for(int j=0;j<y;j++){
            char t[4];
            scanf("%s ",t);
            if(t[0]=='a'||t[0]=='e'||t[0]=='i'||t[0]=='o'||t[0]=='u'||t[0]=='A'||t[0]=='E'||t[0]=='I'||t[0]=='I'||t[0]=='U'||t[0]=='O'){
                strcpy(l[i][j],z[i][j]);
                strcpy(z[i][j],t);
            }
            else
            strcpy(l[i][j],t);
            printf("%s ",z[i][j]);
        }
        printf("\n");
    }
    for(int i=0;i<x;i++){
        for(int j=0;j<y;j++)
        printf("%s ",l[i][j]);
        printf("\n");
    }
}