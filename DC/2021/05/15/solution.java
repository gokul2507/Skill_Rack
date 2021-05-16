import java.text.DecimalFormat;
import java.util.*;
class Person{
    private String s;
    private int w;
    private double h;
    Person(String s,int w,double h){
        this.s=s;
        this.w=w;
        this.h=h;
    }
    public double getBodyMassIndex(){
        return w/(h*h);
    }
    @Override
    public String toString(){
        String H=String.format("%.2f",h);
    return "Name: "+s+"\n"+"Weight: "+w+" kg\n"+"Height: "+H+" m";
    }
}
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