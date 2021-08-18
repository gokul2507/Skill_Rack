#include <stdio.h>
#include <stdlib.h>

void sortAndSplitWords(char *file1name, char *file2name)
{
    char s[101][101];
    int n=0;
    FILE *f1=fopen(file1name,"r"), *f2=fopen(file2name,"r");
    while(fscanf(f1,"%s\n",s[n])==1){
        n++;
    }
    while(fscanf(f2,"%s\n",s[n])==1){
        n++;
    }
    fclose(f1);
    fclose(f2);
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(strcmp(s[i],s[j])>0){
                char temp[101];
                strcpy(temp,s[i]);
                strcpy(s[i],s[j]);
                strcpy(s[j],temp);
            }
        }
    }
    f1=fopen(file1name,"w");
    f2=fopen(file2name,"w");
    for(int i=0;i<n/2;i++){
        if(i==n/2-1) fprintf(f1,"%s",s[i]);
        else fprintf(f1,"%s\n",s[i]);
    }
    for(int i=n/2;i<n;i++){
        fprintf(f2,"%s\n",s[i]);
    }
    fclose(f1);
    fclose(f2);
}

void printFileContent(char *fileName)
{
    FILE *fp = fopen(fileName,"r");
    char ch;
    while((ch = fgetc(fp)) != EOF)
    {
        printf("%c", ch);
    }
    fclose(fp);
}

int main()
{
    char file1name[51], file2name[51];
    scanf("%s\n%s", file1name, file2name);
    sortAndSplitWords(file1name, file2name);
    printf("%s:\n", file1name);
    printFileContent(file1name);
    printf("\n%s:\n", file2name);
    printFileContent(file2name);
    return 0;
}