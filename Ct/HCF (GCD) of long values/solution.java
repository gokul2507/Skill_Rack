import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		long n=q.nextLong(),p=q.nextLong();
		while(n!=p){
		    if(p>n)
		    p-=n;
		    else
		    n-=p;
		}
		System.out.println(n);
	}
}