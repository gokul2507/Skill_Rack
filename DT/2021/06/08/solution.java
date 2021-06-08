import java.util.Scanner;

class Parent {

    private String name;
    private int age;

    public Parent(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void updateAge(int yearsToadd) {
        this.age += yearsToadd;
    }

    public void display() {
        System.out.println(this.name);
        System.out.println(this.age);
    }
} // end of Parent class

class Child extends Parent {

    private String name;
    private int age;

    public Child(String parentName, int parentAge, String childName, int childAge) {
        super(parentName, parentAge);
        this.name = childName;
        this.age = childAge;
    }
    public void updateAge(int x){
        super.updateAge(x);
        this.age+=x;
    }
    public void display(){
        super.display();
        System.out.println(this.name+"\n"+this.age);
    }    
} // end of Child class

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String parentName = sc.nextLine().trim();
        int parentAge = Integer.parseInt(sc.nextLine().trim());
        String childName = sc.nextLine().trim();
        int childAge = Integer.parseInt(sc.nextLine().trim());
        int X = Integer.parseInt(sc.nextLine().trim());
        Child child = new Child(parentName, parentAge, childName, childAge);
        child.updateAge(X);
        child.display();
    } // end of main function
} // end of Hello class
