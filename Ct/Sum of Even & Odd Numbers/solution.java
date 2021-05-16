import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int p=q.nextInt();
		while(p-->0){
		    int o=0,e=0;
		    q.nextInt();
		    q.nextLine();
		    for(String i:q.nextLine().split(" ")){
		        int t=Integer.parseInt(i);
		        if(t%2==0)
		        e+=t;
		        else
		        o+=t;
		    }
		    System.out.println(e+"\n"+o);
		}
	}
