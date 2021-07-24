import java.util.*;
 
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        RegistrationNumberGenerator gen = new RegistrationNumberGenerator();
        int N = Integer.parseInt(sc.nextLine().trim());
        for (int ctr = 1; ctr <= N; ctr++) {
            int year = sc.nextInt();
            char code = sc.nextLine().trim().charAt(0);
            System.out.println(gen.generatRegistrationNumber(year, code));
        }
    }
}

