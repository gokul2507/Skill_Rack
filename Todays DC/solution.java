import java.util.*;
 
public class Hello {
    class City implements Comparable<City>{
        int x,y;
        String n;
        public City(String na,int a,int b){
            x=a;
            y=b;
            n=na;
        }
        @Override
        public int compareTo(City q){
            if(this.x+this.y!=q.x+q.y)
            return -(this.x+this.y-q.x-q.y);
            if(this.x!=q.x)
            return -(this.x-q.x);
            return this.n.compareTo(q.n);
        }
        public String toString(){
            return this.n+" "+this.x+" "+this.y;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());
        List<City> cities = new ArrayList<>();
        for (int ctr = 1; ctr <= N; ctr++) {
            String currCity[] = sc.nextLine().trim().split("\\s+");
            cities.add(new City(currCity[0],
                    Integer.parseInt(currCity[1]),
                    Integer.parseInt(currCity[2])));
        }
        Collections.sort(cities);
        for (City city : cities) {
            System.out.println(city);
        }
    }
}
