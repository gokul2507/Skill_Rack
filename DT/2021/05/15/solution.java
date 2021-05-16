import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner scan=new Scanner(System.in);
		int r=scan.nextInt();
		int c=scan.nextInt();
		String[] a=new String[c];
		Arrays.fill(a,"");
		for(int i=0;i<r;i++)
		{
		    for(int j=0;j<c;j++)
		    {
		        String s=scan.next();
		        a[j]+=s;
		    }
		}
		//System.out.print(Arrays.toString(a));
		long sum=0;
		for(int i=0;i<c;i++)
		{
		    StringBuilder sb=new StringBuilder(a[i]);
		    String t=sb.reverse().toString();
		    sum+=Math.max(Long.parseLong(a[i],2),Long.parseLong(t,2));
		}
		System.out.print(sum);

	}
}