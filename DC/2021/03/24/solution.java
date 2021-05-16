import java.util.*;

interface Pair {

    public long getHCF(int a, int b);

    public boolean areCoPrime(int a, int b);
}
class Node implements Pair{
        public long getHCF(int a, int b){
            if(a==0) return b;
            else return getHCF(b%a,a);
        }
        public boolean areCoPrime(int a, int b){
            if(getHCF(a,b)==1) return true;
            return false;
        }
    }
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        Pair pair = new Node();
        System.out.println("HCF: " + pair.getHCF(a, b));
        System.out.println(pair.areCoPrime(a, b) ? "YES" : "NO");
    }
}
