import java.util.*;
 
public class Hello {
    class Shop{
    HashMap<String,Integer> z;
    public Shop(){
        z=new HashMap<String,Integer>();
    }
    void addItem(String x,int y){
        z.put(x,z.getOrDefault(x,0)+y);
    }
    boolean orderItem(String x,int y){
        if(z.getOrDefault(x,0)>=y){
            z.put(x,z.get(x)-y);
            return 1==1;
        }
        return 1==0;
    }
}
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

