import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());
        List<Train> trains = new ArrayList<>();
        int hh, mm;
        for (int ctr = 1; ctr <= N; ctr++) {
            String currTrain[] = sc.nextLine().trim().split("\\s+");
            Train t = new Train();
            t.setName(currTrain[0]);
            String arrivalTime[] = currTrain[1].split(":");
            String departureTime[] = currTrain[2].split(":");
            hh = Integer.parseInt(arrivalTime[0]);
            mm = Integer.parseInt(arrivalTime[1]);
            t.setArrivalTime(hh, mm);
            hh = Integer.parseInt(departureTime[0]);
            mm = Integer.parseInt(departureTime[1]);
            t.setDepartureTime(hh, mm);
            trains.add(t);
        }
        Collections.sort(trains);
        for (Train train : trains) {
            System.out.println(train.getName() + " " + train.getArrivalTime() + " " + train.getDepartureTime());
        }
    } //end of main method
} //end of Hello class
