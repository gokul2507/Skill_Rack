import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		q.nextLine();
		int o=0,e=0;
		for(String i:q.nextLine().split(" ")){
		    int t=Integer.parseInt(i);
		    if(t%2==0)
		        e+=t;
		    else
		        o+=t;
		}
		System.out.println(o-e);
	}
}
