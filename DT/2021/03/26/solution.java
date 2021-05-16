import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		String a=q.nextLine(),b=q.nextLine(),z="abcdefghijklmnopqrstuvwxyz";
		int a1=0,b1=0;
		while(a1<a.length()){
		    int x=z.indexOf(a.charAt(a1));
		    String t=z.substring(x)+z.substring(0,x);
		    //System.out.println();
		    System.out.print(t.charAt(z.indexOf(b.charAt(b1))));
		    a1++;
		    b1++;
		}
	}
}
