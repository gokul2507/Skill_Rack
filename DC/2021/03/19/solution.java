import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int l=0,n=q.nextInt(),h=q.nextInt();
		for(int i=5;i<=n;i++){
		    String s=Integer.toBinaryString(i);
		    int c=0;
		    while(s.contains("101")){
		        c++;
		        if(c>=h){
		            l++;
		            break;
		        }
		        s=s.substring(s.indexOf("101")+1);
		    }
		}
		System.out.println(l);
	}
}
