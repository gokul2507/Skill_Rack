import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
		StringBuilder s=new StringBuilder(sc.nextLine());
		int a=Integer.parseInt(s.toString());
		int b=Integer.parseInt(s.reverse().toString());
		System.out.print(a-b);
    }
}
