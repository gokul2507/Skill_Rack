import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		int x=q.nextInt(),y=q.nextInt();
		if(y<x)
		y=x;
		for(int i=2;i<n;i++){
		    int t=q.nextInt();
		    int m=y;
		    if(y<x+t)
		    y=x+t;
		    x=m;
		}
		System.out.println(y);
	}
}
