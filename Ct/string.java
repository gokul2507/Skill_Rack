import java.util.*;
public class Hello {

    public static void main(String[] args) {
        String s=new Scanner(System.in).nextLine();
        ArrayList<String> z=new ArrayList<String>();
        for(int i=0;i<s.length();i++){
            for(int j=i+1;j<=s.length();j++){
                String t=s.substring(i,j);
                if(!z.contains(t))
                z.add(t);
            }
        }
        Collections.sort(z);
        System.out.print(z.indexOf(s)+1);
	}
}
