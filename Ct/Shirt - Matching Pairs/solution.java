import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),c=0;
		q.nextLine();
		ArrayList<String> z=new ArrayList<String>(Arrays.asList(q.nextLine().split(" ")));
		for(String i:new HashSet<String>(z)){
		    c+=Collections.frequency(z,i)/2;
		}
		System.out.print(c);
	}
}
