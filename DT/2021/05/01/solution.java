import java.util.*;
public class solution {
    public static void print(String x){
        System.out.print(x);
    }
    public static void main(String[] args) {
		Scanner q =new Scanner(System.in);
		String z[]=q.nextLine().split(" ");
		int n=q.nextInt();
		for(int i=0;i<n;i++){
		    print("*".repeat(i));
		    print((z[3]+" ").repeat(n-i));
		    print((z[0]+" ").repeat(i+1));
		    print((z[1]+" ").repeat(n-i-1));
		    print(z[1]+("*".repeat(i)));
		    print("\n");
		}
		for(int i=0;i<n;i++){
		    print("*".repeat(n+1+i));
		    print((z[2]+" ").repeat(n-i-1));
		    print(z[2]+("*".repeat(n+1+i)));
		    print("\n");
		}
	}
}