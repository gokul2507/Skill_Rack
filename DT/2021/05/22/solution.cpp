#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int x,y;
    cin>>x>>y;
    string z[x][y],l[x][y];
    for(int i=0;i<x;i++){
        for(int j=0;j<y;j++)
        cin>>z[i][j];
    }
    for(int i=0;i<x;i++){
        for(int j=0;j<y;j++){
            string t;
            cin>>t;
            if(t=="a"||t=="e"||t=="i"||t=="o"||t=="u"||t=="A"||t=="E"||t=="I"||t=="O"||t=="U"){
                l[i][j]=z[i][j];
                z[i][j]=t;
            }
            else
            l[i][j]=t;
            cout<<z[i][j]<<" ";
        }
        cout<<endl;
    }
    for(int i=0;i<x;i++){
        for(int j=0;j<y;j++)
        cout<<l[i][j]<<" ";
        cout<<endl;
    }
}