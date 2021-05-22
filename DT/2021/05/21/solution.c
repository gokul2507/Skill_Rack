#include<stdio.h>
#include<stdlib.h>

int main()
{
   int n; scanf("%d",&n); 
   int a[1000],b[1000];
   for(int i=0;i<n;i++) scanf("%d ",&a[i]);
   char s[1000]; scanf("%s",s);
   for(int i=0;s[i]!='\0';i++)
   {
       if(s[i]=='L')
       {
           for(int j=1;j<n;j++)
           {
               if(a[j-1]>0) b[j]++; 
           }
           for(int j=0;j<n;j++) a[j]--;
       }
       else {
           for(int j=0;j<n-1;j++)
           {
               if(a[j+1]>0) b[j]++;
           }
           for(int j=0;j<n;j++) a[j]--;
       }
   }
   for(int i=0;i<n;i++) printf("%d ",b[i]);
}