import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
        int a=q.nextInt(),b=q.nextInt(),c=q.nextInt();
        String s="scalene";
        if(a==b && b==c)
        s="equilateral";
        else{
            if(a==b || b==c || a==c)
            s="isosceles";
        }
        System.out.print(s);
	}
}
