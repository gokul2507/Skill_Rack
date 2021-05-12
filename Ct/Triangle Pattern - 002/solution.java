import java.util.*;
public class Hello {

    public static void main(String[] args) {
		int n=new Scanner(System.in).nextInt();
		for(int i=(n)/2;i>=0;i--)
		System.out.println("!".repeat(i)+"*".repeat(n-i-i)+"!".repeat(i));
	}
}
