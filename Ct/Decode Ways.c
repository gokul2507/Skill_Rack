#include<stdio.h>
#include <stdlib.h>

int main()
{
    char a[100];
    scanf("%s",a);
    int l=strlen(a);
    int dp[l];
    for(int i=0;i<l;i++)
    dp[i]=0;
    if(dp[0]!='0')
    dp[0]=1;
    for(int i=1;i<l;i++){
        int x=a[i]-'0',y=(a[i-1]-'0')*10+(a[i]-'0');
        if(x>=1 && x<10)
            dp[i]+=dp[i-1];
        if(y>9 && y<27)
            if(i-1>0)
                dp[i]+=dp[i-2];
            else
                dp[i]+=1;
    }
    printf("%d",dp[l-1]);
}
