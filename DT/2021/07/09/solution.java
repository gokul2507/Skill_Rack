import java.util.*;
 
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());
        Shop shop = new Shop();
        for (int ctr = 1; ctr <= N; ctr++) {
            String query[] = sc.nextLine().trim().split("\\s+");
            if (query[0].charAt(0) == '+') {
                shop.addItem(query[1], Integer.parseInt(query[2]));
            } else if (query[0].charAt(0) == '-') {
                System.out.println(shop.orderItem(query[1], Integer.parseInt(query[2]))
                        ? "Ordered Successfully" : "Failed");
            }
        }
    }
}

