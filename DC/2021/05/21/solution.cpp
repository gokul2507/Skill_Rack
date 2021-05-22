#include <bits/stdc++.h>
 using namespace std;
int main(int argc, char** argv)
{
    string s;int a[1001],n=0,i,j,b[1001],o=0;
    getline(cin,s);//cout<<s;
    while(scanf("%d ",&a[n])==1)n=n+1;
    if(n!=0){
        for(i=n-1;i>=0;i=i-1)cout<<a[i]<<" ";cout<<s;
    }
    int d=0;
    if(n==0){
        for(i=0;s[i];i=i+1){
            d=0;while(i<s.size()&&isdigit(s[i]))
            d=d*10+s[i]-'0',i=i+1;b[o++]=d;
        }
        for(i=o-1;i>=0;i=i-1)cout<<b[i]<<endl;
    }
}