#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    
    int n ;
    
    cin >> n;
    
    vector<string> vec(n);
    
    for(auto &i : vec)
      cin >> i;
      
      
   char mat[1001][1001];
      
      
   int row = vec[0].size() , ind = 0 , col = 0;
   
   while(ind < n)
   {
       int i = 0 ;
       
       while(i < vec[ind].size())
       {
           for(int j = 0 ; j<row ; j++)
           {
               if(i<vec[ind].size())
                 mat[j][col] = vec[ind][i++];
               else
                 mat[j][col] = '*';
           }
           
           col++;
       }
       
       ind++;
       
   }
   
   for(int i = 0 ; i<row ; i++)
   {
       for(int j = 0 ; j<col ; j++)
         cout << mat[i][j] << " ";
         
       cout << endl;
   }


}