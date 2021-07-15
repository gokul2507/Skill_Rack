#include <stdio.h>
#include <stdlib.h>
 
void findTotalMarks (char *file1name, char *file2name){ 
    FILE *fp1 = fopen (file1name, "r");
    FILE *fp2 = fopen (file2name, "r"); 
    char name[101][101]; 
    int mark[101], i = 0; 
    while (1){   
        int mark1, mark2, mark3;    
        fscanf (fp1, "%s", name[i]);
        fscanf (fp2, "%d %d %d", &mark1, &mark2, &mark3); 
        mark[i++] = mark1 + mark2 + mark3;     
        char c = fgetc (fp1);  
        if (c == EOF)   
        {     
            break;  
        }  
    }
    FILE *fp = fopen (file1name, "w");  
    for (int ind = 0; ind < i; ind++){ 
        fprintf (fp, "%s %d\n", name[ind], mark[ind]);
    }  
    fclose (fp);
}// end of findTotalMarks function
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
    findTotalMarks(file1name, file2name);
    printf("Students and Total Marks:\n");
    printFileContent(file1name);
    return 0;
} // end of main function