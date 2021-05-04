#include <iostream>
#include<string>
using namespace std;
int main(int argc, char** argv)
{
    int n,i,j;
    cin>>n;
    string s,a,b,c;
    for(i=0;i<n;i++){
        cin>>s;   
        a+=s.substr(0,i+1);
        b+=s.substr(i+1,s.length()-2*(i+1));  
        c+=s.substr(s.length()-(i+1));
    }
    cout<<a<<"\n"<<b<<"\n"<<c;
}