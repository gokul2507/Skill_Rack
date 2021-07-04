#include <stdio.h>
#include <stdlib.h>
 
void writeAdjacencyMatrixToFile(int N, int E, int edges[E][2])
{
    
}
void outputAdjacencyMatrixFile()
{
    FILE *fp = fopen("adjacencymatrix.txt","r");
    char ch;
    while((ch = fgetc(fp)) != EOF)
    {
        printf("%c", ch);
    }
    fclose(fp);
}

int main()
{
    int N, E;
    scanf("%d %d", &N, &E);
    int edges[E][2];
    for(int index = 0; index < E; index++)
    {
        scanf("%d %d", &edges[index][0], &edges[index][1]);
    }
    writeAdjacencyMatrixToFile(N, E, edges);
    printf("Adjacency Matrix:\n");
    outputAdjacencyMatrixFile();
    return 0;
}
