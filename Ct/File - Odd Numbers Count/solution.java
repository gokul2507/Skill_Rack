import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.regex.*;
public class Hello {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        try{
            String s=sc.next();
            File f=new File(s);
            int c=0;
            Scanner q=new Scanner(f);
            while(q.hasNextLine()){
                String n=q.nextLine();
                Pattern p=Pattern.compile("[0-9]+");
                Matcher find=p.matcher(n);
                while(find.find()){
                    String s1=find.group();
                    if(Integer.parseInt(s1)%2==1) c++;
                }
            }
            System.out.println(c);
        }
        catch(Exception e){}
	}
}