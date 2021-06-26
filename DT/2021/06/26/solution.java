import java.util.*;
 
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int C = Integer.parseInt(sc.nextLine().trim());
        List<College> colleges = new ArrayList<>();
        for (int collegeCtr = 1; collegeCtr <= C; collegeCtr++) {
            String collegeName = sc.nextLine().trim();
            College college = new College(collegeName);
            String departments[] = sc.nextLine().trim().split("\\s+");
            for (String dept : departments) {
                college.addDepartment(dept);
            }
            colleges.add(college);
        }
        Collections.sort(colleges);
        for (College college : colleges) {
            System.out.println(college.getName());
            for (String dept : college.getDepartments()) {
                System.out.print(dept + " ");
            }
            System.out.println();
        }
    }
}
