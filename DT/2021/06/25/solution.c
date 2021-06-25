#include <stdio.h>
#include <stdlib.h>
 
char* interlaceIntegerAndCharacter(int N, int *arr, char *str)
{
    int l=0;
    char *p=malloc((sizeof(arr)+sizeof(str))*100);
    for(int i=0;i<N;i++){
        char t[1000];
        int q;
        l+=sprintf((p+l),"%d",*(arr+i));
        l+=sprintf((p+l),"%c",*(str+i));
    }
    return p;
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
    char str[N+1];
    scanf("%s", str);
    char *csv = interlaceIntegerAndCharacter(N, arr, str);
    printf("Interlaced String: %s", csv);
    return 0;
}
