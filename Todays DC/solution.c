#include <stdio.h>
#include <stdlib.h>
char *getUniqueUnitDigits(int SIZE,int arr[]){
    char *u=malloc(sizeof(char)*SIZE);
    int l[10]={0};
    for(int i=0;i<SIZE;i++){
        l[arr[i]%10]++;
    }
    int c=0;
    for(int i=9;i>=0;i--){
        if(l[i]!=0) u[c++]=i+'0';
    }
    return u;
}
int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    char *str = getUniqueUnitDigits(N, arr);
    printf("Unique Unit Digits: %s", str);
    free(str);
    return 0;
}
