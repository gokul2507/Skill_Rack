#include <stdio.h>
int main(){
    int n,x,c,s;
    char ch;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        c=0,s=0;
        while(scanf("%d%c",&x,&ch)>0){
            c++,s+=x;
            if(ch=='\n'||ch=='\r') break;
        }
        printf("%d %d\n",c,s);
    }
    return 0;
}