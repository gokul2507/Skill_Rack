import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int y=q.nextInt();
		while(y-->0){
		    int n=q.nextInt(),c=q.nextInt(),f=q.nextInt();
		    int v=n-f+1,a=0;
		    if(v>=c)
		    a=f+c-1;
		    else{
		        int p=n;
		        c-=v;
		        c%=n;
		        if(c==0){
		            c=n;
		        }
		        a=c;
		    }
		    System.out.println(a);
		}
	}
}
