import java.util.Scanner;

public class Hello{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        printPattern(sc.nextInt());
    }
	public static void printPattern(int N) {
		int l=N*(N+1),p=1;
		for(int i=0;i<N;i++){
			System.out.print("-".repeat(2*i));
			for(int j=0;j<N-i;j++)
			   System.out.print((p++)+"*");
			for(int j=0;j<N-i-1;j++)
			   System.out.print((l-N+1+j)+"*");
			System.out.println(l-i);
			l-=N-i-1;
		}
   }
}