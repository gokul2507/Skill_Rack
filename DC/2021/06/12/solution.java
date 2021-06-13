import java.util.*;
public class Hello {
    class Student{
        private String n,c;
        private int a;
        public Student(String n,int a ,String c){
            this.n=n;
            this.a=a;
            this.c=c;
        }
        public boolean equals(Student x){
            if(this.n.equalsIgnoreCase(x.n) && this.c.equalsIgnoreCase(x.c) && this.a==x.a)
                return true;
            return false;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student student1 = getStudent(sc);
        Student student2 = getStudent(sc);
        System.out.println(student1.equals(student2) ? "EQUAL" : "NOT EQUAL");
    } //end of main method

    private static Student getStudent(Scanner sc) {
        String name = sc.nextLine().trim();
        int age = Integer.parseInt(sc.nextLine().trim());
        String country = sc.nextLine().trim();
        return new Student(name, age, country);
    } // end of getCitizen method
} //end of Hello class
