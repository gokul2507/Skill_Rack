#include<stdio.h>
#include<stdlib.h>

int main()
{
  int n,p=0,f=1;
  scanf("%d",&n);
  for(int i=0;i<n;i++){
      int t;
      scanf("%d",&t);
      if(p+1!=t){
        f=0;
        printf("%d-%d ",p+1,t-1);
      }
      p=t;
  }
    if(f)
      printf("-1");
}
