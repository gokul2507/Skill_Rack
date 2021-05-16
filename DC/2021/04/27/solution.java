import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String s=new Scanner(System.in).nextLine();
		int c=0;
		for(int i=1;i<s.length();i++){
    		HashSet<Character> z=new HashSet<Character>();
    		HashSet<Character> q=new HashSet<Character>();
    		for(char j:s.substring(0,i).toCharArray())z.add(j);
    	    for(char j:s.substring(i).toCharArray())q.add(j);
    		if(z.size()==q.size())
    		c++;
		}
		System.out.println(c);
	}
}
