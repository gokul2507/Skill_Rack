import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),z[]=new int[n];
		for(int i=0;i<n;i++){
		    z[i]=q.nextInt();
		}
		for(int i=0;i<n;i++){
		    int t=0;
		    if(i>0)
		    t+=z[i-1];
		    if(i<n-1)
		    t+=z[i+1];
		    System.out.print(t+" ");
		}
	}
}
