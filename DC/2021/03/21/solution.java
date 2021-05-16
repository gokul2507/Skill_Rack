import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int x=q.nextInt(),y=q.nextInt();
		q.nextLine();
		for(int i=0;i<x;i++){
		    String[] z=q.nextLine().split(" ");
		    for(int w=0;w<3;w++){
		        String p="";
		        for(int e=0;e<y;e++){
		            p+=z[e].substring(0,3);
		            z[e]=z[e].substring(3);
		        }
		        for(char e:p.toCharArray())
		        System.out.print(e+" ");
		        System.out.println();
		    }
		}
	}
}
