#include <bits/stdc++.h>  
 using namespace std;
map<long,int>m;
 int main(int argc, char** argv)
{
long long n,sum=0,i,val;
cin>>n;
n=(2*n)+1;
for(i=0;i<n;i++)
{ 
   cin>>val;  
  m[val]=i;
    sum=sum^val;
}
cout<<m[sum]+1; 

}
