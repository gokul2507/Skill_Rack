import java.util.*;
 
class Doctor {
} // end of Doctor class
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String slot[] = sc.nextLine().trim().split("\\s+");
        Doctor doctor = new Doctor(slot[0], slot[1]);
        int N = Integer.parseInt(sc.nextLine().trim());
        for (int ctr = 1; ctr <= N; ctr++) {
            String requestTime = sc.nextLine().trim();
            System.out.print(requestTime + " ");
            System.out.println(doctor.bookAppointment(requestTime)
                    ? "Appointment Scheduled Successfully"
                    : "Failed");
        }
    } // end of main function
} // end of Hello class

