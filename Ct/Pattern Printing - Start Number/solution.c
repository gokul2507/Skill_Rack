#include <stdio.h>
void printPattern(int base, int N)
{
  for(int i=1;i<=N;i++){
      for(int j=0;j<i;j++){
          printf("%d ",base+i-1);
      }
      printf("\n");
  }
  for(int i=N;i>0;i--){
      for(int j=0;j<i;j++){
          printf("%d ",base+i-1);
      }
      printf("\n");
  }
}
int main()
{
    int start, N;
    scanf("%d%d",&start,&N);
    printPattern(start,N);
    return 0;
}
