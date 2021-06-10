import java.util.*;
public class Hello {
    class Person{
        private String n;
        private int a;
        public Person(){
            this.n="person";
            this.a=0;
        }
        public Person(String n){
            this.n=n;
            this.a=0;
        }
        public Person(String n,int a){
            this.n=n;
            this.a=a;
        }
        public String toString(){
            return this.n+':'+this.a;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int query = Integer.parseInt(sc.nextLine().trim());
        Person p = null;
        if (query == 1) {
            p = new Person();
        } else if (query == 2) {
            String name = sc.nextLine();
            p = new Person(name);
        } else if (query == 3) {
            String name = sc.nextLine();
            int age = Integer.parseInt(sc.nextLine().trim());
            p = new Person(name, age);
        }
        System.out.println(p);
    } //end of main method
} //end of Hello class