import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		ArrayList<String> z=new ArrayList<String>();
		while(n-->0){
		    q.nextLine();
		    String s=q.next();
		    if(q.nextInt()+q.nextInt()+q.nextInt()>149)
		    z.add(s);
		}
		Collections.sort(z);
		for(String i:z)
		System.out.println(i);
	}
}