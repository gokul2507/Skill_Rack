#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int n ; 
    cin>>n; 
    int arr[n],ans[n]; 
    memset(ans,0,sizeof(ans));
    for(int & i : arr)cin>>i;
    string str;
    cin>>str;
    for(char ch : str){
        if(ch=='L'){
            for(int i= 1 ;i < n ;i++){
                if(arr[i-1]>0){
                    arr[i-1]--;
                    ans[i]++;
                }
            }
            arr[n-1]--;
        }
        else{
            arr[0] --;
            for(int i = 0 ;i +1 < n ;i++){
                if(arr[i+1]>0){
                    arr[i+1]--;
                    ans[i]++;
                }
            }
        }
    }
    for(int i : ans)
        cout<<i<<" ";
}