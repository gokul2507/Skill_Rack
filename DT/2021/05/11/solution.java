import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int a=q.nextInt(),t=0,z[]=new int[a];
		for(int i=0;i<a;i++){
		    z[i]=q.nextInt();
		    t=Math.max(t,z[i]);
		}
		for(int i=0;i<t;i++){
		    for(int j:z){
		        String s="* ".repeat(j);
		        if(i+1<=j)
		        s=(j+" ").repeat(j);
		        System.out.print(s);
		    }
		    System.out.println();
		}
	}
}