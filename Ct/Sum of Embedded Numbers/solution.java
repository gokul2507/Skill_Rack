import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int s=0,t=0;
		for(char i:q.nextLine().toCharArray()){
		    if(Character.isDigit(i))
		    t=t*10+(i-'0');
		    else{
		        s+=t;
		        t=0;
		    }
		}
		System.out.println(s+t);
	}
}
