import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		String a=q.nextLine();
		int x=q.nextInt();
		for(int i=1;i<a.length()+x;i++){
		    String t="*".repeat(Math.max(0,i-x))+a.substring(Math.max(0,i-x),Math.min(i,a.length()))+"*".repeat(Math.max(0,a.length()-i));
		    StringBuilder m=new StringBuilder(t.substring(0,a.length()-1));
		    m=m.reverse();
		    System.out.println(t+m);
		}
	}
}