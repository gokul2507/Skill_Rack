import java.util.*;
public class Hello {
    public static void main(String[] args) {
        //Your Code Her
        Scanner q=new Scanner(System.in);
        int n=q.nextInt(),s=0;
        q.nextLine();
        String z[]=q.nextLine().split(" ");
        for(String i:z){
            char t[]=i.toCharArray();
            Arrays.sort(t);
            s+=Integer.parseInt(t[t.length-1]+""+i+""+t[0]);
        }
        System.out.println(s);
    }
}