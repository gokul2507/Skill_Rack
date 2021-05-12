import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		for(int i=0;i<n;i++){
		    String s="Yes";
		    if(q.nextInt()%4==1)
		    s="No";
		    System.out.println(s);
		}
	}
}
