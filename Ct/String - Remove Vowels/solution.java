import java.util.Scanner;
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        char strval[] = removeVowels(input.toCharArray(), input.length());
        
        for(Character ch:strval){
            System.out.print(ch);
        }
    }
    static char[] removeVowels(char[] input, int LENGTH) {
        String s="";
        for(char i:input)
        if(!"aeiouAEIOU".contains(i+""))
        s+=i+"";
        return s.toCharArray();
 }
}