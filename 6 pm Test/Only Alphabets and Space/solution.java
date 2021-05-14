import java.util.*;
public class Hello {

    public static void main(String[] args) {
        char[] z=new Scanner(System.in).nextLine().toCharArray();
        for(char i:z)
        if(Character.isAlphabetic(i) || i==' ')
        System.out.print(i);
	}
}