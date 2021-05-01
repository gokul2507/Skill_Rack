import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int r=q.nextInt(),c=q.nextInt();
		for(int i=0;i<c;i++){
		    for(int k=0;k<r;k++){
		            for(int l=0;l<c*r;l++){
		                String t="1";
		                if((i+l/r)%2==0)
		                t="0";
		                System.out.print(t+" ");
		            }
		            System.out.println();
		        }
		    
		}
	}
}