import java.util.*;
 
public class Hello {
    class Rectangle implements Comparable<Rectangle>{
        int l,b,a;
        public Rectangle(int x,int y){
            l=x;
            b=y;
            a=x*y;
        }
        public String toString(){
            return l+" "+b+" "+a;
        }
        
        @Override
        public int compareTo(Rectangle x){
            if(this.a!=x.a){
                return -this.a+x.a;
            }
            return -this.b+x.b;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        List<Rectangle> values = new ArrayList<>();
        for (int ctr = 1; ctr <= N; ctr++) {
            int length = sc.nextInt();
            int breadth = sc.nextInt();
            values.add(new Rectangle(length, breadth));
        }
        Collections.sort(values);
        for (Rectangle rect : values) {
            System.out.println(rect);
        }
    }
}
