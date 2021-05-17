import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		
		boolean ans=true;
		
		if(n%2==0)
		ans=false;
		
		
		int st=1;
		char c='a';
		for(int i=0;i<n;i++)
		{
		    for(int j=0;j<n;j++)
		    {
		        if(ans)
		            System.out.print(st);
		        else
		            System.out.print(c);
		            
		        st++;
		        c++;
	            if(c>'z')
	            c='a';
	        
		        System.out.print(" ");
		    }
		    System.out.println();
		    ans=!ans;
		}

	}
}