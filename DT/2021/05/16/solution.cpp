#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int n ; 
    cin>>n; 
    int val = 1;
    for(int i = 0 ;i < n ;i++){
        for(int j = 0 ;j < n ;j++){
            if(i%2==n%2)
                cout<<char((val-1)%26+'a');
            else
                cout<<val;
            cout<<" ";
            val++;
        }
        cout<<endl;
    }

}