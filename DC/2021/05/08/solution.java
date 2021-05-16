import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		String s1=q.nextLine(),s2=q.nextLine();
		int l1=s1.length(),l2=s2.length(),t1=l1/2,t2=l2/2,p=0;
		if(s1.charAt(t1+p)!=s2.charAt(t2+p)){
		    System.out.println("-1");
		    return;
		}
		while(t1+p<l1 && t2+p<l2){
		    if(!(s1.charAt(t1+p)==s2.charAt(t2+p) && s1.charAt(t1-p)==s2.charAt(t2-p)))
		    break;
		    p++;
		}
		System.out.println(s1.substring(t1-p+1,t1+p));
	}
}