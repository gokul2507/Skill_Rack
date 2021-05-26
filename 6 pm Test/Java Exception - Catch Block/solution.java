import java.util.*;

public class Hello {

    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        try{
            System.out.println(Integer.parseInt(input));
        }
        catch(Exception e){
            System.out.print("NOTANINTEGER");
        }

    }//end of main method

}//end of class Hello
