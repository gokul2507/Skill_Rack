#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int r,c;
    cin>>r>>c;
    char arr[r][c];
    for(int i= 0 ;i < r;i++)
        for(int j = 0 ;j< c;j++)
            cin>>arr[i][j];
    string str;
    cin>>str;
    int n = str.size();
    for(int i = 0 ;i < r;i++){
        for(int j= 0 ;j< c;j++){
            for(int x = 1 ; x<=n;x++){
                if(n%x)continue;
                for(int y = 1 ; y<=n ;y++){
                    if(n/x%y)continue;
                    string temp = "";
                    for(int a = i ;a<i+x && a<r ;a++){
                        for(int b = j ;b<j+y && b<c ;b++){
                            temp.push_back(arr[a][b]);
                        }
                    }
                    if(temp==str){
                        for(int a = i ; a<i+x;a++){
                            for(int b = j ; b<j+y ;b++)
                                cout<<arr[a][b]<<" ";
                            cout<<endl;
                        }
                        return 0;
                    }
                }
            }
        }
    }

}