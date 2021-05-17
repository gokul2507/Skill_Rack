#include<stdio.h>
void main(){
    int N;
    scanf("%d\n",&N);
    for(int ctr=0;ctr<N;ctr++){
        int len=0,sum=0,p;
        char c;
        while(1){
            scanf("%d%c",&p,&c);
            len++;
            sum+=p;
            if(c=='\r'||c=='\n')
            break;
        }
        printf("%d %d\n",len,sum);
    }
}