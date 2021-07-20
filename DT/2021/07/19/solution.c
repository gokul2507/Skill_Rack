#include <stdio.h>
#include <stdlib.h>
#include<string.h>
void transposeMatrix(char *fileName)
{
    FILE *fp = fopen(fileName,"r");
    char temp[1001];
    int mat[1001][1001];
    int k=0,l=0;
    while(fgets(temp,1001,fp)!=NULL)
    {
        char *tok = strtok(temp," ");
        l=0;
        while(tok!=NULL)
        {
            int val = atoi(tok);
            mat[k][l++] = val;
            tok = strtok(NULL," ");
        }
        k++;
    }
    fp = fopen(fileName,"w");
    for(int i=0;i<l;i++)
    {
        for(int j=0;j<k;j++)
        {
            fprintf(fp,"%d ",mat[j][i]);
        }
        fprintf(fp,"%c",'\n');
    }
    fclose(fp);
}
void printFileContent(char *fileName)
{
    FILE *fp = fopen(fileName, "r");
    char ch;
    while((ch = fgetc(fp)) != EOF)
    {
        printf("%c", ch);
    }
    fclose(fp);
} // end of printFileContent function

int main()
{
    char fileName[31];
    scanf("%s", fileName);
    transposeMatrix(fileName);
    printf("Transpose Matrix:\n");
    printFileContent(fileName);
    return 0;
} // end of main function