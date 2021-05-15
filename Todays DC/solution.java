import java.text.DecimalFormat;
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine().trim();
        int weight = sc.nextInt();
        double height = sc.nextDouble();
        Person person = new Person(name, weight, height);
        System.out.println(person);
        System.out.printf("BMI: %.1f", person.getBodyMassIndex());
    }
}