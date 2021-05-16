#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
    int n,i,j;
    cin>>n;
    int x,y,f=1,f1=1,f2=1;
    x=n-1;
    y=n;
    char arr[n*2][n*2];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n*2;j++)
        {
            if(x==j && f==1)
            {
                arr[i][j]='/';
                x--;
                f=0;
            }
            else if(y==j && f1==1)
            {
                arr[i][j]='\\';
                y++;
                f1=0;
            }
            else
                arr[i][j]='#';
            if(f2==0 && f1!=0)
            if(i>1)
            {
                arr[i][j]=arr[i-2][j];
            }
            if(f==0)
                f2=0;
        }
        f=1;f1=1;f2=1;
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n*2;j++)
        {
            cout<<arr[i][j];
        }
        cout<<"\n";
    }
    for(i=n-1;i>=0;i--)
    {
        for(j=0;j<n*2;j++)
        {
            if(arr[i][j]=='#')
                cout<<"#";
            else if(arr[i][j]=='/')
                cout<<"\\";
            else
                cout<<"/";
        }
        cout<<"\n";
    }
    return 0;
}
