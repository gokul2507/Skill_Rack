import java.util.*;
class SkillRackException extends Exception{
    public SkillRackException(String s){
        super(s);
    }
}
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        try {
            throw new SkillRackException(input);
        } catch (SkillRackException sre) {
            System.out.println(sre.getMessage());
        }

    }//end of main method

}//end of class Hello