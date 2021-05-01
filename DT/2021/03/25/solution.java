import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String z=new Scanner(System.in).nextLine();
		int m=0,s=0,e=0,t=0,i=1;
		for(;i<z.length();i++){
		    if((z.charAt(i)-'0')%2==(z.charAt(i-1)-'0')%2){
		        if(m<i-t){
		            s=t;
		            e=i;
		            m=i-t;
		        }
		        t=i;
		    }
		}
		if(m<i-t){
		    s=t;
		    e=i;
		}
		System.out.println(z.substring(s,e));
	}
}
