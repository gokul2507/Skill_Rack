#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    string str;
    cin>>str;
    sort(str.begin(),str.end());
    int ans = 0 ; 
    for(int i = 0 ;i < str.size() ;i++){
        if(i==0){
            if(str[0]==str[1]-1)
                ans++;
        }
        else if(i==str.size()-1){
            
        }
        else if(str[i-1]+1!=str[i] && str[i]+1==str[i+1]){
            ans++;
        }
    }
    
    cout<<(ans?ans:-1);

}