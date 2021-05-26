#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int n,a,count=0;
    cin>>n>>a;
    for(int i=n;i>=1;i/=2)
    {
        if(i % a ==0) count++;
    }
    cout<<count;
}