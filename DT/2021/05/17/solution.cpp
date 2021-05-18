#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int r,c;
    cin>>r>>c;
    int arr[r][c];
    for(int i= 0 ;i < r;i++)for(int j = 0 ;j < c;j++)cin>>arr[i][j];
    int k; cin>>k;
    int f = k-1,l =k;
    while(f>-1 || l<r){
        for(int j= 0 ; j < c;j++){
        int val = 0; 
        if(f>-1)
            val+=arr[f][j];
        if(l<r)
            val+=arr[l][j];
        cout<<val<<" ";
        }
        cout<<endl;
        f--;
        l++;
    }

}