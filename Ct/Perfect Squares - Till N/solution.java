import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        printSquare(N);

    }
    static void printSquare(int n) {
        int c=1,x=1;
        while(x<=n){
            System.out.print(x+" ");
            c+=1;
            x=c*c;
        }
    }
}