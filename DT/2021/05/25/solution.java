public import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner scan=new Scanner(System.in);
		String s=scan.next();
		int ans=0;
		int[] a=new int[26];
		for(int i=0;i<s.length();i++)
		{
		    a[s.charAt(i)-'a']++;
		}
		for(int i=0;i<26;i++)
		{
		    if(a[i]!=0)
		    {
    		    int in=i+1;
    		    while(in<26 && a[in]!=0)
    		    {
    		        in++;
    		    }
    		    if(i!=in-1)
    		    ans++;
    		    i=in-1;
		    }
		}
		System.out.print(ans==0?-1:ans);

	}
}class solution {
    
}
