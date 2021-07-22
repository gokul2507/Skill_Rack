import java.util.*;
 
public class Hello {
    class Test implements Comparable<Test>{
        String a,b;
        int c,w;
        public Test(String x,String y,int z){
            a=x;
            b=y;
            c=z;
            String[] p=y.split(":");
            w=Integer.parseInt(p[0])*100+Integer.parseInt(p[1]);
        }
        @Override
        public int compareTo(Test q){
            if(this.w!=q.w)
            return this.w-q.w;
            if(this.c!=q.c)
            return this.c-q.c;
            return this.a.compareTo(q.a);
        }
        public String toString(){
            return this.a+" "+this.b+" "+this.c;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        List<Test> tests = new ArrayList<>();
        for (int ctr = 1; ctr <= N; ctr++) {
            String currTest[] = sc.nextLine().trim().split("\\s+");
            tests.add(new Test(currTest[0], currTest[1],
                    Integer.parseInt(currTest[2])));
        }
        Collections.sort(tests);
        for (Test test : tests) {
            System.out.println(test);
        }
    } // end of main function
} // end of Hello class

