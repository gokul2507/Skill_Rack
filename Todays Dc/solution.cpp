#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int x,y,a,b;
    cin>>x>>y;
    int z[x][y];
    for(int i=0;i<x;i++)
    for(int j=0;j<y;j++)
    cin>>z[i][j];
    cin>>a>>b;
    for(int i=0;i<y;i++)
    cout<<z[a-1][i]*z[b-1][y-1-i]<<" ";
}