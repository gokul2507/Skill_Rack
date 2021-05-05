#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
    string s;cin>>s;
    char a,b;
    cin>>a;
    cin>>b;
    int m=s.length(),flag=0,d=0;
    for(int i=0;i<s.length();i++){   
        if(s[i]==a||s[i]==b)  
        { 
            if(flag==1&&d!=0)   
            {       
                if(d<m)    
                m=d;  
                d=0;  
            }  
            else     
            flag=1; 
        }   
        if(flag==1) 
        d++;
    }
    cout<<m-1;
}