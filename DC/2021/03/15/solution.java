import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		String[] s=q.nextLine().split(" ");
		int n=q.nextInt();
		if(n<0)
		n=s.length+n+1;
		n--;
		while(n>0 && (!s[n-1].contains(".")))
		n--;
		while(n<s.length){
		    System.out.print(s[n]+" ");
		    if(s[n].contains("."))
		    break;
		    n++;
		}
	}
}
