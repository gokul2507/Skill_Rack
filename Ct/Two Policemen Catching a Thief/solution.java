import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		while(n-->0){
		    int a=q.nextInt(),b=q.nextInt(),c=q.nextInt();
		    String s="Police";
		    a-=c;
		    b-=c;
		    if(a<0)
		    a=-a;
		    if(b<0)
		    b=-b;
		    if(a<b)
		    s+="1";
		    else if(b<a)
		    s+="2";
		    else
		    s="Both";
		    System.out.println(s);
		}
	}
}
