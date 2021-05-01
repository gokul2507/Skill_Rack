import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		while(n-->0){
		    int x=q.nextInt(),t=x%5;
		    if(x<38 || t==0)
		    t=0;
		    else if(t>2)
		    x+=5-t;
		    System.out.println(x);
		}
	}
}
