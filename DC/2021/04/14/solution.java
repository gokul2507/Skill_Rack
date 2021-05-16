import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String a=new Scanner(System.in).nextLine();
		int i=a.length()-1;
		while(i>=0){
		    int t=(int)a.charAt(i);
		    if(t%2==1)
		    break;
		    i--;
		}
		if(i==-1){
		    System.out.println("0");
		    return;
		}
		System.out.print(a.substring(0,i+1));
	}
}
