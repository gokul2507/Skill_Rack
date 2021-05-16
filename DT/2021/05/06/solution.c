#include<stdio.h>
#include<stdlib.h>

int main()
{ 
    int n; 
    scanf("%d",&n); 
    char s[100][100]; 
    for(int i=0;i<n;i++){
        scanf("%s\n",&s[i]);
    }
    char a[100][100]; int j_in=0; 
    int r=strlen(s[0]);
    for(int i=0;i<n;i++){ 
        int ind=0; 
        while(ind<strlen(s[i])){
        for(int j=0;j<r;j++){
            a[j][j_in]=s[i][ind++]; 
        } 
        j_in++;
        }
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<j_in;j++){
            if(isalpha(a[i][j])){
                printf("%c ",a[i][j]);
            }
            else{
                printf("* ");
            }
        }
        printf("\n");
    }

}