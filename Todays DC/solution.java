import java.util.*;
public class Hello {
    class Student{
        private String s;
        private int m;
        public Student(String s,int m){
            this.s=s;
            this.m=m;
        }
        public void addExtraMarks(int x){
            this.m+=x;
            if(this.m>100) this.m=100;
        }
        public String toString(){
            return this.s+":"+this.m;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        List<Student> students = new ArrayList<>();
        for (int ctr = 1; ctr <= N; ctr++) {
            String studentDetails[] = sc.nextLine().trim().split("\\s+");
            students.add(new Student(studentDetails[0], Integer.parseInt(studentDetails[1])));
        }
        for (Student stud : students) {
            stud.addExtraMarks(sc.nextInt());
            System.out.println(stud);
        }
    }
}
