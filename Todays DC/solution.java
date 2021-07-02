import java.util.Scanner;
 
class Student implements College, Department {

    public void printStudentName(String name) {
        System.out.println("Name: " + name);
    }

    @Override
    public void printDepartmentName(String name) {
        System.out.println("Department: " + name);
    }

    @Override
    public void printCollegeName(String name) {
        System.out.println("College: " + name);
    }
} // end of Student class
interface College{
    public void printStudentName(String n);
    public void printCollegeName(String c);
}
interface Department{
    public void printDepartmentName(String d);
}
public class Hello {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        Student stud = new Student();
        stud.printStudentName(sc.nextLine());
        stud.printDepartmentName(sc.nextLine());
        stud.printCollegeName(sc.nextLine());
    } // end of main function
} // end of Hello class
