#include <iostream>
using namespace std;
int main()
{
    char s[11],s1[11];
    cin>>s;
    int l=strlen(s);
    for(int i=l-1,j=0;i>=0,j<l;i--,j++) s1[j]=s[i];
    cout<<atoi(s)-atoi(s1);
}
