import java.util.*;
public class Hello {
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		int c=0,z[]=new int[n];
		for(int i=0;i<n;i++){
		    z[i]=q.nextInt();
		    if(i<2)
		    continue;
		    if(z[i-1]>z[i-2]&&z[i-1]>z[i]){
		        c++;
		    }
		}
		System.out.println(c);
	}
}
