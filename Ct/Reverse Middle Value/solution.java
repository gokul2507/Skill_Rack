[7:00 PM, 3/21/2021] Gokul R: import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		q.nextLine();
		while(n-->0){
		    StringBuilder s=new StringBuilder(q.nextLine());
		    System.out.print(s.charAt(0));
		    s.reverse();
		    System.out.println(s.substring(1,s.length()-1)+s.charAt(0));
		}
	}
}
[7:01 PM, 3/21/2021] Rex Milton clg: 
