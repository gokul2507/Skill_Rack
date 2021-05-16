import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int sum=0,z=q.nextInt(),x=q.nextInt(),y=q.nextInt();
		while(x<=y){
		    if(x%z==0)
		    sum+=x;
		    x++;
		}
		System.out.println(sum);
	}
}
