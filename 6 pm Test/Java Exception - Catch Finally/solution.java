import java.util.*;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        try {
            if(input.length() > 5){
                throw new Exception("TooLong");
            }
        }
        catch(Exception e){
            System.out.println("TooLong");
        }
        finally{
            System.out.println(input);
        }
}//end of main method

}//end of class Hello