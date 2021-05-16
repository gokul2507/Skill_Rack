import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),f=0,p=0;
		for(int i=0;i<n;i++){
		    int t=q.nextInt();
		    if(p+1!=t){
		        f=1;
		        System.out.print((p+1)+"-"+(t-1)+" ");
		    }
		    p=t;
		}
		if(f==0)
		System.out.println(-1);
	}
}
