#include<stdio.h>
#include<stdlib.h>
int ch(char s[])
{
    if(s[0]>='0'&&s[0]<='9')
    return 0;
    return 1;
    
}
int main()
{
    int y,i,j,x,k,c;
    scanf("%d %d\n",&x,&y);
    char a[55][55][10],b[55][55][10];
    for(i=0;i<x;i++,scanf("\n"))
    for(j=0;j<y;j++)
    scanf("%s ",a[i][j]);
for(j=0;j<y;j++)
{
    c=0;
    for(i=0;i<x;i++)
    {
        if(ch(a[i][j]))
        {
            strcpy(b[c++][j],a[i][j]);
        }
    }
    for(i=0;i<x;i++)
    if(!ch(a[i][j]))
    strcpy(b[c++][j],a[i][j]);
}
for(i=0;i<x;i++,printf("\n"))
for(j=0;j<y;j++)
printf("%s ",b[i][j]);

}