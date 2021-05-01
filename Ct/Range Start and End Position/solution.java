import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
        q.nextLine();
        ArrayList<String> z=new ArrayList<String>();
        z.add("-");
        for(String i:q.nextLine().split(" "))
        z.add(i);
        String t=q.nextLine();
        System.out.println((z.indexOf(t))+" "+(z.lastIndexOf(t)));
	}
}
