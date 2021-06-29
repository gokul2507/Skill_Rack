import java.util.*;
public class Hello {
        public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int s=sc.nextInt();
        sc.nextLine();
        String a="";
        for(int i=0;i<s;i++){
            a+=sc.nextLine();
            System.out.println(a);
            a=a.substring(0,i+1);
        }
    }
}