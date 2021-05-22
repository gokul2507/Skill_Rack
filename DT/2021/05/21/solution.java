import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
Scanner in=new Scanner(System.in);
int n=in.nextInt();int arr[]=new int[n];
for(int i=0;i<n;i++)
arr[i]=in.nextInt();
int t[]=new int[n];
String s=in.next();
for(char c:s.toCharArray())
{
    if(c=='L')
    {
        for(int i=0;i<n;i++)
        {
            int t1=arr[i];
            if(t1==0)
            continue;
            arr[i]--;
            if(i+1<n)
            t[i+1]++;
            
        }
    }
    else
    {
        for(int i=n-1;i>=0;i--)
        {
            int t1=arr[i];
            if(t1==0)
            continue;
            arr[i]--;
            if(i-1>=0)
            t[i-1]++;
        }
    }
}
for(int i:t)
System.out.print(i+" ");
	}
}