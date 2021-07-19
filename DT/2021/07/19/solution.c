#include <stdio.h>
#include <stdlib.h>
 
void transposeMatrix(char *fileName)
{
    
} // end of transposeMatrix function
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