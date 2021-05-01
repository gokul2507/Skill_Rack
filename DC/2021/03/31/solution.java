import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int c=0,a=q.nextInt(),b=q.nextInt();
		while(a>0 || b>0){
		    if(a%2!=b%2)
		    c++;
		    a/=2;
		    b/=2;
		}
		System.out.print(c);
	}
}
