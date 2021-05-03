import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
        int n=q.nextInt(),t=0,s=0;
        while(n-->0){
            t=q.nextInt();
            if(t>9 && t<100)
            s+=t;
        }
        System.out.println(s);
	}
}