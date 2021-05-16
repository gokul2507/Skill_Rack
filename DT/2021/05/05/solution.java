import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		ArrayList<String> ar=new ArrayList<>();
		String[] c=new String[n];
		Arrays.fill(c,"");
		for(int i=0;i<n;i++)
		{
		    String t="";
		    for(int j=0;j<n;j++)
		    {
		        char ch=scan.next().charAt(0);
		        t+=ch;
		        c[j]+=t.charAt(j);
		    }
		    ar.add(t);
		}
		ArrayList<String> ar2=new ArrayList<>();
		for(int i=0;i<n;i++)
		{
		    ar2.add(c[i]);
		}
		
		String u=scan.next();
		String v=scan.next();
		
// 		if((ar.contains(u) && ar.contains(v)) || (ar2.contains(u) && ar2.contains(v)))
		
		if(find(ar,u,v) || find(ar2,u,v))
		System.out.print("YES");
		else
		System.out.print("NO");
		
		

	}
	static boolean find(ArrayList<String> ar,String a,String b)
	{
	    int i=0,j=0;
	    for(String s:ar)
	    {
	        StringBuilder sb=new StringBuilder(s);
	        String s2=sb.reverse().toString();
	        if(i==0 && (s.contains(a) || s2.contains(a)))
	        i++;
	        else if(s.contains(b) || s2.contains(b))
	        j++;
	        if(i!=0 && j!=0)
	        return true;
	    }
	    return false;
	}
}