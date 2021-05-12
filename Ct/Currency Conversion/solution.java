import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		while(n-->0){
		    System.out.printf("%.02f\n",q.nextInt()*q.nextFloat());
		}
	}
}
