import java.util.*;
public class Hello {
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		String z[][]=new String[n][n];
		q.nextLine();
		for(int i=0;i<n;i++){
		    z[i]=q.nextLine().split(" ");
		}
		for(int i=0;i<n/2;i++){
		    String t=z[i][i];
		    z[i][i]=z[i][n-i-1];
		    z[i][n-i-1]=z[n-i-1][n-i-1];
		    z[n-i-1][n-i-1]=z[n-i-1][i];
		    z[n-i-1][i]=t;
		}
		for(int i=0;i<n;i++){
		    for(String j:z[i])
		    System.out.print(j+" ");
		    System.out.println();
		}
	}
}