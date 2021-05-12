import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        printPattern(N);
    }
private static void printPattern(int N) {
    int c=1;
    for(int i=1;i<=N;i++){
        if(i%2!=0)
        for(int j=0;j<i;j++)
        System.out.print(c+++" ");
        else{
            c+=i;
            for(int j=c-1;j>=c-i;j--)
            System.out.print(j+" ");
        }
        System.out.println();
    }
}
} // end of class
