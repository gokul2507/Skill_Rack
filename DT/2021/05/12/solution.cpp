#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    
    int r , c ;
    
    cin >> r >> c;
    
    char mat[r][c];
    
    for(int i = 0 ; i<r ; i++)
    {
        for(int j = 0 ; j<c ; j++)
          cin >> mat[i][j];
    }
    
    string s;
    
    cin >> s;
    
    int ind = 1 , flag = 0;
    
    loop:
        for(int i = 0 ; i<r ; i++)
        {
            for(int j = 0 ; j<c ; j++)
            {
                if(flag && ind<s.size())
                   mat[i][j] = s[ind++];
                else if(mat[i][j]==s[0])
                    flag = 1;
            }
        }
    
    if(ind < s.size())
       goto loop;


    for(int i = 0 ; i<r ; i++)
    {
        for(int j = 0 ; j<c ; j++)
          cout << mat[i][j] << " ";
        
        cout << endl;
    }

}