#include <bits/stdc++.h>
 
using namespace std;

int r,c;
vector<vector<int>> mat;

long long int dec(string t)
{
    long long int val=0;
    for(int i=0;i<t.length();i++)
        val+=(t[i]-'0')*pow(2,t.length()-1-i);
    return val;
}

void find()
{
    long long int sum=0;
    for(int i=0;i<c;i++)
    {
        string t="";
        for(int j=0;j<r;j++)
        {
            t+=(mat[j][i]+'0');
        }
        long long int val1=dec(t);
        reverse(t.begin(),t.end());
        long long int val2=dec(t);
        sum+=max(val1,val2);
    }
    cout<<sum;
}

int main(int argc, char** argv)
{
    cin>>r>>c;
    mat.resize(r,vector<int>(c));
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            cin>>mat[i][j];
    find();
}