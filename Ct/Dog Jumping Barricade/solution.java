import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		while(n-->0){
		    int x=q.nextInt(),y=q.nextInt(),z=q.nextInt(),t,c=0;
		    while(z-->0){
		        t=q.nextInt();
		        while(1==1){
		            t-=x;
		            c++;
		            if(t<=0)
		            break;
		            t+=y;
		        }
		    }
		    System.out.println(c);
		}
	}
}
