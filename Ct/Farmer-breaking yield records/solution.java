import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),w=q.nextInt(),wc=0,bc=0,b=0;
		b=w;
		while(n-->1){
		    int t=q.nextInt();
		    if(t>b){
		        b=t;
		        bc++;
		    }
		    if(t<w){
		        w=t;
		        wc++;
		    }
		}
		System.out.print(bc+" "+wc);
	}
}
