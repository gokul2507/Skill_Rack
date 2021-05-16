import java.util.*;
public class Hello {

    public static void main(String[] args) {
		int n=new Scanner(System.in).nextInt();
		String t="";
		for(int i=1;i<=n;i++){
		    String s=i+"";
		    s=s.repeat(i);
		    System.out.println(s);
		    t="\n"+s+t;
		}
		System.out.println(t.substring(1));
	}
}