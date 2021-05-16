#include <iostream>
using namespace std;
int main(){
  int n,td;
  cin>>n;
  char c[n];
  int a[n];
  for(int i=0;i<n;i++) cin>>c[i];
  for(int i=0;i<n;i++) cin>>a[i];
  cin>>td;
  int d=1,r=0,g=0,b=0;
  while(d<=td){
      for(int i=0;i<n;i++){
          if(c[i]=='R' && a[i]>0){ r++; a[i]--;}
          else if(c[i]=='G' && a[i]>0 && d%2==0) { g++; a[i]--;}
          else if(c[i]=='B' && a[i]>0 && d%3==0){ b++; a[i]--;}
      }
      d++;
  }
  cout<<r<<" "<<g<<" "<<b;
}
