import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String s=new Scanner(System.in).nextLine();
		for(int i=0;i<s.length();i++)
		System.out.println(s.substring(i,i+1).repeat(i+1));
	}
}