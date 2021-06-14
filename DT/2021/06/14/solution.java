import java.util.*;
public class Hello {
    class Theatre{
        int[][] z;
        int s;
        public Theatre(){
            z=new int[100][2];
            s=0;
        }
        public boolean book(int a,int b){
            if(s==0){
                z[s][0]=a;
                z[s][1]=b;
                s++;
                return 1==1;
            }
            for(int i=0;i<s;i++){
                int x=z[i][0];
                int y=z[i][1];
                //System.out.println(a+" "+b+" "+x+" "+y);
                if((x<=a && a<=y)||(x<=b && b<=y)||(a<=x && y<=b))
                return 1==0;
            }
            z[s][0]=a;
            z[s][1]=b;
            s++;
            return 1==1;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Theatre theatre = new Theatre();
        for (int ctr = 1; ctr <= N; ctr++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            System.out.println(theatre.book(start, end) ? "Successful" : "Failed");
        }
    } //end of main method
} //end of Hello class
