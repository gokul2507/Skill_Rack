import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int r=q.nextInt(),c=q.nextInt();
		for(int i=0;i<r;i++){
		    int t=0;
		    for(int j=0;j<c;j++){
		        t+=q.nextInt();
		    }
		    System.out.println(t);
		}
	}
}