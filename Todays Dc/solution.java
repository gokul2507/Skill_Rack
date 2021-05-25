import java.util.*;
public class Hello {
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),t=q.nextInt(),c=0;
		String a=Integer.toBinaryString(n);
		for(int i=1;i<=a.length();i++){
		    if(Integer.parseInt(a.substring(0,i),2)%t==0)
		    c++;
		}
		System.out.println(c);
	}
}