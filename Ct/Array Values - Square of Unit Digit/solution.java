import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		while(n-->0){
		    int t=q.nextInt()%10;
		    System.out.print(t*t+" ");
		}
	}
}
