#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int r,c;
    cin>>r>>c;
    queue<string> cold[c],cola[c];
    for(int i = 0 ;i < r;i++){
        for(int j = 0 ;j< c;j++){
            string str;
            cin>>str;
            if(isalpha(str[0]))
                cola[j].push(str);
            else
                cold[j].push(str);
        }
    }
    for(int i = 0 ;i< r;i++){
        for(int j = 0 ;j < c;j++){
            if(cola[j].empty())
                cout<<cold[j].front(),cold[j].pop();
            else
                cout<<cola[j].front(),cola[j].pop();
            cout<<" ";
        }
        cout<<endl;
    }

}