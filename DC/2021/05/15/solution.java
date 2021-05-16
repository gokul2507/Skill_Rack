import java.text.DecimalFormat;
import java.util.*;
class Person{
    String name;
    int weight;
    double height;
    Person(String name,int weight,double height){
        this.name=name;
        this.weight=weight;
        this.height=height;
    }
    float getBodyMassIndex(){
        return weight/((float)(height*height));
    }
    public String toString(){
        return "Name: "+name+"\nWeight: "+weight+" kg\nHeight: "+String.format("%.2f m",height);
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