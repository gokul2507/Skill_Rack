import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		q.nextLine();
		String s1="",s2="",s3="";
		for(int i=0;i<n;i++){
		    String t=q.nextLine();
		    s1+=t.substring(0,i+1);
		    s2+=t.substring(i+1,t.length()-i-1);
		    s3+=t.substring(t.length()-i-1);
		}
		System.out.println(s1+"\n"+s2+"\n"+s3);
	}
}