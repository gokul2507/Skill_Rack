import java.util.*;
public class Hello {
    static double x;
    static boolean square(double n){
        double t=Math.sqrt(x);
        return (int)(t)==t;
    }
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		x=q.nextDouble();
		boolean f=false;
		double y=q.nextDouble();
		while(x<=y){
		    if(square(x)){
		        if(f)
		        System.out.print(",");
		        System.out.print((int)(x));
		        f=true;
		    }
		    x++;
		}
	}
}
