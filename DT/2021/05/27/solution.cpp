#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int r,c;
    cin>>r>>c;
    char arr[r][c];
    for(int i = 0 ;i < r;i++)
        for(int j = 0 ;j< c;j++)
            cin>>arr[i][j];
    int ans = 0 ; 
    bool flag = 1;
    while(flag){
        flag = 0;
        ans++;
        if(ans&1){
            for(int i = 0 ;i < r;i++){
                for(int j= c-1 ; j>-1 ;j--){
                    if(arr[i][j]=='#' &&((i+1<r && arr[i+1][j]=='#')
                    ||(i-1>-1 && arr[i-1][j]=='#')))
                        break;
                    if(arr[i][j]=='#'){
                        arr[i][j]='*';
                        if(j)
                            arr[i][j-1]='*';
                        break;
                    }
                }
            }
        }
        else{
            for(int j = 0 ;j < c;j++){
                for(int i = r-1 ;i>-1 ;i--){
                    if(arr[i][j]=='#' && ((j+1<c && arr[i][j+1]=='#')
                    || (j-1>-1 && arr[i][j-1]=='#')))
                        break;
                    if(arr[i][j]=='#'){
                        arr[i][j]='*';
                        if(i)
                            arr[i-1][j] = '*';
                        break;
                    }
                }
            }
        }
        for(int i = 0 ;i< r;i++){
            for(int j = 0 ;j< c;j++){
                if(arr[i][j]=='#')flag = 1;
                // cout<<arr[i][j]<<" ";
            }
            // cout<<endl;
        }
    }
    cout<<ans;

}