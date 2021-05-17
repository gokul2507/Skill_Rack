#include<stdio.h>
#include <stdlib.h>
int main()
{ 
    int n,d,t,c=0,x=1,h=1,f=1,a[1000];   
    scanf("%d %d",&n,&d);  
    scanf("%d",&t);   
    a[0]=0;   
    for(int i=1;i<t;i++){   
        a[x]=f*n;   
        if(x==1) a[1]++;  
        f=f+(f*n);  
        c++;   
        if(c>=d){    
            f=f-a[h];  
            h++;  
        }   
        x++; 
    }
    printf("%d",f);
}