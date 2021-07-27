#include <stdio.h>
#include <stdlib.h>
void swapFileContent(char *file1name, char *file2name)
{
    rename(file1name,"file1");
    rename(file2name,file1name);
    rename("file1",file2name);
} // end of swapFileContent function
void printFileContent(char *filename)
{
    FILE *fp = fopen(filename,"r");
    char ch;
    while((ch = fgetc(fp)) != EOF)
    {
        printf("%c", ch);
    }
    fclose(fp);
} // end of printFileContent function

int main()
{
    char file1name[31], file2name[31];
    scanf("%s\n%s", file1name, file2name);
    swapFileContent(file1name, file2name);
    printf("File %s:\n", file1name);
    printFileContent(file1name);
    printf("\nFile %s:\n", file2name);
    printFileContent(file2name);
    return 0;
} // end of main function