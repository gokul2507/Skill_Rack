#include<stdio.h>
#include <stdlib.h>
int count(long int x,int c){ 
    if(x==1)  
    return c;  
    if(x%2){   
        int t=count(x-1,c+1);   
        int p=count(x+1,c+1);    
        if(t<p)     
        return t;  
        return p; 
    } 
    else{  
        return count(x/2,c+1);   
    }
}
int main()
{ 
    long int n;  
    scanf("%ld",&n); 
    printf("%d",count(n,0));
}
