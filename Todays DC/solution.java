import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());
        List<Event> events = new ArrayList<>();
        for (int ctr = 1; ctr <= N; ctr++) {
            String currEvent[] = sc.nextLine().trim().split("\\s+");
            String title = currEvent[0];
            int registrationFee = Integer.parseInt(currEvent[1]);
            int duration = Integer.parseInt(currEvent[2]);
            events.add(new Event(title, registrationFee, duration));
        }
        Collections.sort(events);
        for (Event event : events) {
            System.out.println(event);
        }
    }
}