import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int a=q.nextInt();
		q.nextLine();
		ArrayList<String> z=new ArrayList<String>();
		String t=q.nextLine();
		int l=t.length();
		z.add(t);
		for(int i=1;i<a;i++){
		    t=q.nextLine();
		    while(t.length()>0){
		        z.add(t.substring(0,Math.min(l,t.length()))+"*".repeat(l-Math.min(t.length(),l)));
		        t=t.substring(Math.min(t.length(),l));
		    }
		}
		for(int i=0;i<l;i++){
		    for(String j:z)
		    System.out.print(j.charAt(i)+" ");
		    System.out.println();
		}
	}
}